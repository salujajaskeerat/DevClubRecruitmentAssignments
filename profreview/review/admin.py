from django.contrib import admin
from .models import *
# Register your models here.


class CommentAdmin(admin.ModelAdmin):
	list_display=('user','prof','anonymous','like','timestamp')
	list_filter=('prof','anonymous','like','timestamp')
	search_fields=('user','prof','content')


class LikedAdmin(admin.ModelAdmin):
	list_display=('user','comment','created')

class ProffAdmin(admin.ModelAdmin):
	list_display=('Name','department','course')
	list_filter=('department','course')
class ratingAdmin(admin.ModelAdmin):
	list_display=('user','prof','rating1')
	list_filter=('prof','rating1')
	
admin.site.register(Proff,ProffAdmin)
admin.site.register(Profile)
admin.site.register(department)

admin.site.register(Comment,CommentAdmin)
admin.site.register(prof_review,ratingAdmin)
admin.site.register(Liked,LikedAdmin)


# Customization of Admin interface
admin.site.site_header='Admin Panel (ProffReviews)'