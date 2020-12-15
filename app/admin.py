from django.contrib import admin
from app.models import Place,District,State,Season,Place_type,Top_list

# Register your models here.


admin.site.register(Place)
admin.site.register(District)
admin.site.register(State)
admin.site.register(Season)
admin.site.register(Place_type)
admin.site.register(Top_list)