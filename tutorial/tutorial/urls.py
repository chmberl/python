from django.conf.urls import include, url
from rest_framework import routers
from snippets import views
from django.contrib import admin
from django.contrib.auth.models import User, Group
admin.autodiscover()

from rest_framework import permissions, routers, serializers, viewsets
# from oauth2_provider.ext.rest_framework import (TokenHasReadWriteScope,
                                                # TokenHasScope)


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User


# class GroupSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Group


# class UserViewSet(viewsets.ModelViewSet):
#     permissions_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class GroupViewSet(viewsets.ModelViewSet):
#     permissions_classes = [permissions.IsAuthenticated, TokenHasScope]
#     required_scopes = ['groups']
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer

# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)
# router.register(r'groups', GroupViewSet)

urlpatterns = [
    # Examples:
    # url(r'^$', 'tutorial.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^', include(router.urls)),
    url(r'^sineppets/', include("snippets.urls")),
    url(r'^api-auth/',
        include('rest_framework.urls',
                namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^api/example/', views.ExampleView.as_view()),
]
