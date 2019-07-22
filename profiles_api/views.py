from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API view"""
    def get(self, request, format=None):
        """Returns a list of API features"""
        an_apiview = [
            'Uses HTTP methods as functions(get, post, patch, put, delete)',
            'Is similar to a traditional django view',
            'Gives you most control over application logic',
            'It is ammped manually to urls',
        ]

        return Response({'message':'hello', 'an_apiview': an_apiview})
