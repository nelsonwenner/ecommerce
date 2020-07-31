from rest_framework_simplejwt import views as jwt_views
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from .views import *

urlpatterns = [

    path('', ApiRoot.as_view(), name=ApiRoot.name),

    path('address', AddressListView.as_view(), name=AddressListView.name),
    path('address/<str:pk>', AddressDetail.as_view(), name=AddressDetail.name),

    path('clients', ClientListView.as_view(), name=ClientListView.name),
    path('clients/<str:pk>', ClientDetail.as_view(), name=ClientDetail.name),

    path('status', StatusListView.as_view(), name=StatusListView.name),
    path('status/<str:pk>', StatusDetail.as_view(), name=StatusDetail.name),

    path('categories', CategoryListView.as_view(), name=CategoryListView.name),
    path('categories/<str:pk>', CategoryDetail.as_view(), name=CategoryDetail.name),

    path('products', ProductListView.as_view(), name=ProductListView.name),
    path('products/<str:pk>', ProductDetail.as_view(), name=ProductDetail.name),

    path('checkouts', CheckoutListView.as_view(), name=CheckoutListView.name),
    path('checkouts/<str:pk>', CheckoutDetail.as_view(), name=CheckoutDetail.name),

    path('checkoutitems', CheckoutItemListView.as_view(), name=CheckoutItemListView.name),
    path('checkoutitems/<str:pk>', CheckoutItemDetail.as_view(), name=CheckoutItemDetail.name),

    path('paymentmethods', PaymentMethodListView.as_view(), name=PaymentMethodListView.name),

    path('paymentgateways', PaymentGatewayListView.as_view(), name=PaymentGatewayListView.name),
    
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api-token/refresh', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    
]

