from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views

router = DefaultRouter()
# basename is for retrieving url
# querysetがないviewsetを使うときはbasenameが必要
router.register("hello-viewset", views.HelloViewSet, basename="hello-viewset")
# base nameは不要(viewsetにはquerysetがあるから)
router.register("profile", views.UserProfileViewset)

urlpatterns = [
    path("hello-view/", views.HelloApiView.as_view()),
    path("login/", views.UserLoginApiView.as_view()),
    path("", include(router.urls)),
]
