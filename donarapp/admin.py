from donarapp.models import Snippet
from django.contrib import admin
from .models import Snippet,Data
# Register your models here.
admin.site.register(Snippet)
admin.site.register(Data)