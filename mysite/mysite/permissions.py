from blog.models import Article
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
#
# content_type = ContentType.objects.get_for_model(Article)
#
# permission = Permission.objects.create(codename='can_publish', name='Can Publish Article', content_type=content_type)