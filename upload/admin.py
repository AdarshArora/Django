from django.contrib import admin

# Register your models here.
from .models import FileUpload
from .models import Post

admin.site.register(FileUpload)
admin.site.register(Post)
