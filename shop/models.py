from django.db import models


class Order(models.Model):

    '''The order model is linked to the customer via id.
     You can specify the created_at date yourself.'''

    id = models.IntegerField(primary_key=True)
    product = models.CharField(max_length=100)
    created_date = models.DateField()

    def __str__(self):
        '''The function returns the model of the car for the convenience of displaying in the admin panel.'''
        return self.product


class Customer(models.Model):
    '''The customer model describes the basic information about the customer.
      You can specify the birth_date and registration_date date yourself.'''
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    birth_date = models.DateField()
    registration_date = models.DateField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        '''The function returns the driver's name for easy display in the admin panel.'''
        return self.first_name


