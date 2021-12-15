from django.contrib import admin
from django.urls import path, reverse
from django.shortcuts import render
from .models import Customer, Order
from django import forms
from django.contrib import messages
from django.http import HttpResponseRedirect
from datetime import datetime


class CsvImportForm(forms.Form):
    csv_upload = forms.FileField()


class CustomerAdmin(admin.ModelAdmin):
    # List of names to display in the admin panel
    list_display = ('first_name', 'last_name', 'birth_date', 'registration_date', 'order')

    # Function for getting a new url
    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv),]
        return new_urls + urls

    # Function for loading csv files
    def upload_csv(self, request):
        '''We check if the POST method, load the file, check the format for compliance.
        If not csv - display the message 'The wrong file type was uploaded'.
        If yes, we display a message 'Your csv file has been imported'.'''
        if request.method == "POST":
            csv_file = request.FILES["csv_upload"]

            if not csv_file.name.endswith('.csv'):
                messages.warning(request, 'The wrong file type was uploaded')
                return HttpResponseRedirect(request.path_info)

            self.message_user(request, "Your csv file has been imported")
            # Read the file, encode it in utf-8, chew it up on a new line
            file_data = csv_file.read().decode("utf-8")
            csv_data = file_data.split("\n")
            # Iterate over line by line
            for x, row in enumerate(csv_data):
                # Checking a null string to skip
                if x==0:
                    pass
                # Checking the second condition so as not to go beyond the bounds of list.
                elif x < (len(csv_data)-1):
                    row = "".join(row)
                    row = row.replace(",", " ")
                    row = row.split()
                    birthday = row[2]
                    # Changing the time format
                    birthday = datetime.strptime(birthday, "%Y/%m/%d").strftime('%Y-%m-%d')
                    registration = row[3]
                    registration = datetime.strptime(registration, "%Y/%m/%d").strftime('%Y-%m-%d')
                    Customer.objects.update_or_create(
                        first_name=row[0],
                        last_name=row[1],
                        birth_date=birthday,
                        registration_date=registration)
            url = reverse('admin:index')
            return HttpResponseRedirect(url)

        form = CsvImportForm()
        data = {"form": form}
        return render(request, "admin/csv_upload.html", data)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'created_date')


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)



