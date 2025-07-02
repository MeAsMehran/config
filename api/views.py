from rest_framework.generics import ListAPIView , RetrieveAPIView , ListCreateAPIView , RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render , get_object_or_404
from blog.models import Article
from .serializers import ArticleSerializer , UserSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from .permissions import IsSuperUser , IsStaffOrReadOnly , IsAuthorOrReadOnly , IsSuperUserOrStaffReadOnly      # we create a permission file for more custom permissions we want for our website
from rest_framework.authentication import SessionAuthentication



# Create your views here.
# we can create classes and methods for viewing (RetrieveApiView) and updating(UpdateApiView) for example instead of (UpdateRetrieveApiView)
class ArticleList(ListCreateAPIView):
    queryset = Article.objects.all()        # the variable name should be this (queryset). creating a queryset for showing in as json or api
    # def get_queryset(self):
    #     print("==================================")
    #     print(self.request.user)
    #     print(self.request.auth)
    #     print("==================================")
    #     return Article.objects.all()

    serializer_class = ArticleSerializer    # the variable name should be this (serializer_class)
    # authentication_classes = (SessionAuthentication, )      # We have some general authentications in setting.py and some specific ones only for some views like here


class ArticleDetail(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = "pk"                     # It tells the view which model field to use when looking up an object in the database. By default, DRF uses the pk (primary key) to look up objects from the URL
    permission_classes = (IsStaffOrReadOnly, IsAuthorOrReadOnly)        # IsStaffOrReadOnly permission is for viewing the articles and IsAuthorOrReadOnly only let the user only can modify his own article and not others
    # authentication_classes = (SessionAuthentication, )


class UserList(ListCreateAPIView):
    queryset = User.objects.all()        # the variable name should be this (queryset). creating a queryset for showing in as json or api
    serializer_class = UserSerializer    # the variable name should be this (serializer_class)
    # permission_classes = (IsAdminUser, )      # We have some general permissions and some specific permissions (the comma , is necessary when we set single permissions)
    # permission_classes = (IsAdminUser, IsSuperUser, IsSuperUserOrStaffReadOnly)
    permission_classes = (IsSuperUserOrStaffReadOnly, )     # this permission let SuperUser(admin to see the users and change their details) and Staff(mehran) to read only the details. And Staff not to see user details


class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
#     permission_classes = (IsAdminUser,)
#     permission_classes = (IsAdminUser, IsSuperUser, IsSuperUserOrStaffReadOnly)
    permission_classes = (IsSuperUserOrStaffReadOnly, )


# With APIView you can send Response by specifying the methods like get, post, put and delete to do what you want. In this way we DON'T USE GENERIC VIEWS LIKE ABOVE!
# For below class we only need delete method and we send our response.
# Response need json as argument
# This method deletes the user Token
# class RevokeToken(APIView):
#     permission_classes = (IsAuthenticated, )
#
#     # def get(self, request):
#     #     return Response({"method" : "get"})
#     #
#     # def post(self, request):
#     #     return Response({"method" : "post"})
#     #
#     # def put(self, request):
#     #     return Response({"method" : "put"})
#
#     def delete(self, request):
#         request.auth.delete()
#         return Response({"msg" : "Token Revoked!"}, status=204)     # the reason msg Token Revoked! not appears is because 204 as status is no content which show no content as response



# articleDetail -> retrieve
# articleUpdate -> update
# articleDelete -> Destroy

# /1/delete/
# /1/update

# rewrite the api views codes for app views using templates