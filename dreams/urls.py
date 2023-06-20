from django.urls import path
from dreams.views import UserLoginAPIView, UserRegistrationAPIView,ProductAPIView,ProductUpdateDeleteAPIView,MerchantAPIView

urlpatterns = [
    path('login/', UserLoginAPIView.as_view(), name='api-login'),
    path('register/', UserRegistrationAPIView.as_view(), name='api-register'),
    path('product/', ProductAPIView.as_view(), name='product'),
    path('update_product/', ProductUpdateDeleteAPIView.as_view(), name='update_product'),
    path('merchant/', MerchantAPIView.as_view(), name='merchant'),
]
