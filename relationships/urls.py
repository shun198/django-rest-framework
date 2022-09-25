from django.urls import path, include
from rest_framework_nested import routers
from .views import CustomerViewSets,BookViewSets

# Create a router and register our viewsets with it.
router = routers.DefaultRouter()
router.register(r'customers', CustomerViewSets,basename="customer")
customer_router = routers.NestedDefaultRouter(router,r"customers",lookup="customer")
customer_router.register(r'books', BookViewSets, basename='book')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path(r'', include(router.urls)),
    path(r'', include(customer_router.urls)),
]
