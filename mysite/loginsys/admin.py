from django.contrib import admin
from loginsys.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    fields = ['user', 'sex', 'avatar']
    list_filter = ['user']
    search_fields = ['user']
    # list_display = ('article_title', 'article_text', 'article_date', 'article_update', 'article_user',
    #                 'article_category', 'article_image')


admin.site.register(Profile, ProfileAdmin)
