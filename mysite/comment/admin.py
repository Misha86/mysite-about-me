from django.contrib import admin
from comment.models import Comments


class CommentAdmin(admin.ModelAdmin):
    list_display = ['comments_article', 'comments_create', 'comments_text', 'comments_user']
    search_fields = ['comments_text', 'comments_article']
    # radio_fields = {'comments_article': admin.VERTICAL}
    # raw_id_fields = ['comments_article', ]
    list_per_page = 20


admin.site.register(Comments, CommentAdmin)