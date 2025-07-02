from django.shortcuts import render , get_object_or_404
from django.views.generic import TemplateView
from django.shortcuts import redirect

from allauth.account.mixins import (
    AjaxCapableProcessFormViewMixin,
    CloseableSignupMixin,
    LogoutFunctionalityMixin,
    NextRedirectMixin,
    RedirectAuthenticatedUserMixin,
    _ajax_response,
)
from allauth import app_settings
from allauth.account import app_settings
from django.http import Http404 , HttpResponse
from allauth.account.adapter import get_adapter
# Create your views here.

from django.views.generic import ListView , DetailView
from .models import Article

# Search about the ListView and other View attributes
class ArticleList(ListView):
    def get_queryset(self):     # method name should be get_queryset because of ListView
        return Article.objects.filter(status=True)



class ArticleDetail(DetailView):
    model = Article
    context_object_name = 'article'     # Name of the object in the template context. Default is 'object'.
    def get_object(self, queryset=None):
        return get_object_or_404(Article.objects.filter(status=True),
                                 pk=self.kwargs.get("pk"))


