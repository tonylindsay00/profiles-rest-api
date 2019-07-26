from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializer


class HelloApiView(APIView):
    """Test API view"""
    serializer_class = serializer.HelloSerializer


    def get(self, request, format=None):
        """Returns a list of API features"""
        an_apiview = [
            'Uses HTTP methods as functions(get, post, patch, put, delete)',
            'Is similar to a traditional django view',
            'Gives you most control over application logic',
            'It is ammped manually to urls',
        ]

        return Response({'message':'hello', 'an_apiview': an_apiview})

    def post(self,request):
        """Create a hellomessage with our name """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(selk, request,pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handlea partial update of an object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Handles deleting an object"""
        return Response({'method': 'DELETE'})
