from django.urls import path, include
from rest_framework_nested import routers
from relationships.views import (
    BookViewSets,
    AuthorViewSets,
    CustomerViewSets,
    WorkplaceViewSets,
    BankViewSets,
    health_check,
    # CreateTokenView,
)
from relationships.user_views import (
    UserViewSet,
)
from rest_framework_simplejwt.views import TokenVerifyView

# Create a router and register our viewsets with it.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'books', BookViewSets,basename="book")
router.register(r'authors', AuthorViewSets,basename="author")
router.register(r'customers', CustomerViewSets,basename="customer")
router.register(r'workplaces',WorkplaceViewSets,basename="workplace")
router.register(r'banks', BankViewSets,basename="bank")
# customer_router = routers.NestedDefaultRouter(router,r"customers",lookup="customer")
# customer_router.register(r'books', BookViewSets, basename='book')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path(r'', include(router.urls)),
    # path(r'', include(customer_router.urls)),
    path("health/", health_check, name="health"),
    # path("token/", CreateTokenView.as_view(), name="token"),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
