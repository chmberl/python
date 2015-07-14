from django.conf.urls import include, url
from rest_framework import routers
from quickstart import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    # Examples:
    # url(r'^$', 'tutorial.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include("snippets.urls")),
    #url(r'^api-auth/', include('rest_framework.urls',
    #    namespace='rest_framework')),
    #url(r'^', include(router.urls)),
    url(r'^api-auth/',
        include('rest_framework.urls',
                namespace='rest_framework'))
]
