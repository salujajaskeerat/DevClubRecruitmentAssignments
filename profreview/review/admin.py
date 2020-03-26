from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Proff)
admin.site.register(Profile)
admin.site.register(department)

class CommentAdmin(admin.ModelAdmin):
	list_display=('user','prof','anonymous','like','timestamp')
	list_filter=('prof','anonymous','like','timestamp')
	search_fields=('user','prof','content')

admin.site.register(Comment,CommentAdmin)
admin.site.register(prof_review)
admin.site.register(Liked)


# Customization of Admin interface
admin.site.site_header='Admin Panel (ProffReviews)'