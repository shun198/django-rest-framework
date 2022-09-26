from urllib import request
from rest_framework.views import APIView
from rest_framework import viewsets
# Use to return response
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers

class HelloApiView(APIView):
    """Test API VIew"""
    serializer_class = serializers.HelloSerializer
    def get(self,request,format=None):
        """Return a list of APIView features"""
        an_apiview = [
            "Uses HTTP methods as function(GET,POST,PATCH,PUT.DELETE)",
            "Is similar to a traditional Django View",
            "Gives you the most control over your application logic",
            "Is mapped manually to URLs",
        ]
        
        return Response({"message":"Hello","an_apiview":an_apiview})
    
    def post(self,request):
        """Create a hello message with our name"""
        # self.serializer_classはserializerクラスをviewで使うときのベストプラクティス
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f"Hello {name}"
            return Response({"message":message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
            
    def put(self,request,pk=None):
        """Handle updating an object"""
        return Response({"method":"PUT"})
    
    def patch(self,request,pk=None):
        """Handle a partial update of an object"""
        return Response({"method":"PATCH"})
    
    def delete(self,request,pk=None):
        """Delete an object"""
        return Response({"method":"DELETE"})
    
class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    # APIViewと違ってHTTPメソッドではなく、下記のメソッドを使う
    def list(self,request):
        """Return a hello message"""
        a_viewset = [
            "Uses actions(list,create,retrieve,update,partial_update)",
            "Automatically maps to URLs using Routers",
            "Provides more functionality with less code", 
        ]
        return Response({"message":"Hello!","a_viewset":a_viewset})