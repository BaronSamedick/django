from django.urls import path
from rest_framework.routers import SimpleRouter

from main_app import views

router = SimpleRouter()
router.register(r'home', views.PostViewSet)

urlpatterns = [
    path('post/', views.posts),
]

urlpatterns += router.urls
