from django.contrib import admin
from django.urls import path, include
from country import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'api', views.CountryViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]