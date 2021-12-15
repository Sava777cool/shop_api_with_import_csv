from rest_framework import generics, filters
from .serializers import CustomerSerializer
from .models import Customer


class CustomersList(generics.ListCreateAPIView):
    '''Displaying a list of all customers. Class complete POST and GET requests.'''
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    '''Customers are filtered by the registration_date field in the YYYY-m-d format'''
    filter_backends = [filters.SearchFilter]
    search_fields = ['registration_date']




