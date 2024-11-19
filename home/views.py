from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import BlogSerializer

class BlogView(APIView):
    authentication_classes = [JWTAuthentication]  # Enforce JWT-based authentication
    permission_classes = [IsAuthenticated]  # Allow only authenticated users

    def post(self, request):
        try:
            data = request.data
            serializer = BlogSerializer(data=data)

            if not serializer.is_valid():
                return Response({
                    'data': serializer.errors,
                    'message': 'Validation failed for blog data.',
                }, status=status.HTTP_400_BAD_REQUEST)
            
            serializer.save(user=request.user)  # Assign the currently logged-in user to the blog

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
