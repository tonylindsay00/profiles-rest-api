from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from profiles_api import serializer
from profiles_api import models, serializer
from profiles_api import permissions


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


class HelloViewSet(viewsets.ViewSet):
    """Test API Viewset"""
    serializer_class = serializer.HelloSerializer

    def list(self, request):
        """Returns a hello message"""

        a_viewset = [
            'Uses actions(list, create, retrieve, update, partial_update)',
            'Automaticall maps to URLs using Routers',
            'provides more functionality with less code',
        ]

        return Response({'message': 'Hello', 'a_viewset': a_viewset})

    def create(self, request):
        """Crete a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request,pk=None):
        """Handles getting an object by its ID"""
        return Response({'http_method': 'GET'})

    def update(self, request,pk=None):
        """Handles updating an object by its ID"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request,pk=None):
        """Handles updating part of an object by its ID"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request,pk=None):
        """Handles deleting an objectobject by its ID"""
        return Response({'http_method': 'DELETE'})



class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating, creating and updating profiles"""
    serializer_class = serializer.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authenticatio_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authenticaion tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
