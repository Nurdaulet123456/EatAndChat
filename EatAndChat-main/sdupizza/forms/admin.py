from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Form)
admin.site.register(Image)
admin.site.register(Stock)
admin.site.register(Order)
admin.site.register(Customer)
admin.site.register(OrderItem)
admin.site.register(Address)


