from django.contrib import admin
from blog.models import Article, Tag
from navigation.models import Category, MenuItem
from comment.models import Comments
from django.utils.translation import ugettext_lazy as _


class ArticleInLine(admin.TabularInline):
    model = Comments
    extra = 2


class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['article_title', 'article_slug', 'article_text', 'article_user', 'article_category',
                           'article_tag', 'article_likes']}),
        (_('Зававнтажені картинки'), {'fields': ['article_image', ]})
    ]
    list_filter = ['article_date', 'article_update']
    search_fields = ['article_title']
    list_display = ('article_title', 'article_text', 'article_date', 'article_user',
                    'article_category', 'article_image', 'get_absolute_url')
    prepopulated_fields = {"article_slug": ("article_title",)}
    list_filter = ['article_category', 'article_date', ]
    list_per_page = 20
    inlines = [ArticleInLine]


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"tag_name": ("tag_title",)}


admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag, TagAdmin)
