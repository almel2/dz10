from django.contrib import admin

from polls.models import City, Product, Provider, User

admin.site.register(City)
admin.site.register(User)
admin.site.register(Product)
admin.site.register(Provider)
