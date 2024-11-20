from rest_framework import serializers
from home.models import Blog

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['uuid','title', 'blog_text', 'main_image', 'created_at', 'updated_at']

