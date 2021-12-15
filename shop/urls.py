from django.urls import path, include
from .views import CustomersList


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('customers/', CustomersList.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]