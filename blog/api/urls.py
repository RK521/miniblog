from django.urls import path, include
from blog.api import views 
from rest_framework.routers import  DefaultRouter

router = DefaultRouter()
router.register('crud',views.DestinationViewSet, basename='user')


urlpatterns = [
    path('', include(router.urls )),
    
]

