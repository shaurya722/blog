from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.db.models import Q
from .serializers import BlogSerializer
from home.models import Blog
from django.core.paginator import Paginator

class BlogView(APIView):
    authentication_classes = [JWTAuthentication]  
    permission_classes = [IsAuthenticated] 

    def get(self, request):
        try:
            objs = Blog.objects.filter(user=request.user).order_by('?')

            search = request.GET.get('search', None)
            if search:
                objs = objs.filter(
                    Q(title__icontains=search) | Q(blog_text__icontains=search)
                )

            print(f"Filtered QuerySet: {objs}")
            # serializer = BlogSerializer(objs, many=True)

            page_number = request.GET.get('page',1)
            paginator = Paginator(objs,2)
            serializer = BlogSerializer(paginator.page(page_number),many= True)


            return Response({
                'data': serializer.data,
                'message': 'Blogs fetched successfully.',
            }, status=status.HTTP_200_OK)

        except Exception as e:
            print(f"Error: {e}")
            return Response({
                'data': {},
                'message': 'something went wrong or Invalid Page',
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

    def post(self, request):
        try:
            data = request.data
            serializer = BlogSerializer(data=data)

            if not serializer.is_valid():
                return Response({
                    'data': serializer.errors,
                    'message': 'Validation failed for blog data.',
                }, status=status.HTTP_400_BAD_REQUEST)
            
            serializer.save(user=request.user) 
            return Response({
                'data': serializer.data,
                'message': 'Blog post created successfully.',
            }, status=status.HTTP_201_CREATED)
        
        except Exception as e:
            print(f"Error: {e}")
            return Response({
                'data': {},
                'message': 'An error occurred while creating the blog post.',
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def patch(self, request):
        try:
            data = request.data

            blog = Blog.objects.filter(uuid=data.get('uuid')).first()

            if not blog:
                return Response({
                    'data': {},
                    'message': 'Invalid blog uid.',
                }, status=status.HTTP_400_BAD_REQUEST)

            if request.user != blog.user:
                return Response({
                    'data': {},
                    'message': 'You are not authorized to update this blog.',
                }, status=status.HTTP_400_BAD_REQUEST)

            serializer = BlogSerializer(blog, data=data, partial=True)

            if not serializer.is_valid():
                return Response({
                    'data': serializer.errors,
                    'message': 'Validation failed for blog data.',
                }, status=status.HTTP_400_BAD_REQUEST)

            serializer.save() 

            return Response({
                'data': serializer.data,
                'message': 'Blog updated successfully.',
            }, status=status.HTTP_200_OK)

        except Exception as e:
            print(f"Error: {e}")
            return Response({
                'data': {},
                'message': 'An error occurred while updating the blog.',
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

      
    def delete(self, request):
        try:
            # Extract UUID from the request (assuming it's sent in the body or query params)
            uuid = request.data.get('uuid') or request.query_params.get('uuid')

            # Check if UUID was provided
            if not uuid:
                return Response({
                    'data': {},
                    'message': 'UUID is required to delete a blog.',
                }, status=status.HTTP_400_BAD_REQUEST)

            # Fetch the blog post by UUID
            blog = Blog.objects.filter(uuid=uuid).first()

            if not blog:
                return Response({
                    'data': {},
                    'message': 'Blog with the provided UUID does not exist.',
                }, status=status.HTTP_404_NOT_FOUND)

            # Check if the logged-in user is the owner of the blog
            if request.user != blog.user:
                return Response({
                    'data': {},
                    'message': 'You are not authorized to delete this blog.',
                }, status=status.HTTP_403_FORBIDDEN)

            # Delete the blog post
            blog.delete()

            return Response({
                'data': {},
                'message': 'Blog deleted successfully.',
            }, status=status.HTTP_200_OK)

        except Exception as e:
            print(f"Error: {e}")
            return Response({
                'data': {},
                'message': 'An error occurred while deleting the blog.',
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)