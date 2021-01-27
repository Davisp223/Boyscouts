from django.contrib import admin
from .models import Post
from .models import Patch
from .models import Feedback
# Register your models here.

admin.site.register(Post)
admin.site.register(Patch)
admin.site.register(Feedback)
