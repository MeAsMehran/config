from django.urls import path , include , re_path
from django.views.generic import TemplateView
from .views import ArticleList , ArticleDetail , UserDetail , UserList
from api import templates

app_name = "api"

urlpatterns = [
    path("article/", ArticleList.as_view(), name="list"),
    path("article/<int:pk>", ArticleDetail.as_view(), name="detail"),     # because of the ArticleRetrieve using DetailRetrieve we can use <"int:pk"> easily here without doing more in views method
    path("users/", UserList.as_view(), name="user-list"),
    path("users/<int:pk>", UserDetail.as_view(), name="user-detail"),

    # re_path(
    #     r'^account-confirm-email/(?P<key>[-:\w]+)/$', TemplateView.as_view(template_name='account _confirm.html'),
    #     name='account_confirm_email',
    # ),

]