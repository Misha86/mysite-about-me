from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
import os


def upload_location(instance, filename):
    path = 'upload/profile_images'
    profile = Profile.objects.order_by("user_id").last()
    if instance.user_id is not None:
        return os.path.join(path, str(instance.user_id), str(filename))
    if not profile:
        return os.path.join(path, 'FIRST_Profile', str(filename))
    if profile.user_id is not None:
        new_id = profile.user_id + 1
        return os.path.join(path, str(new_id), str(filename))


class Profile(models.Model):
    class Meta:
        db_table = "profile"
        verbose_name = _("Профіль користувача")
        verbose_name_plural = _("Профілі користувачів")

    user = models.OneToOneField(User, primary_key=True, related_name="profile", verbose_name=_("Користувач"),
                                on_delete=models.CASCADE)
    sex = models.CharField(max_length=20, choices=(('Man', _('Чоловік')), ('Woman', _('Жінка'))),
                           verbose_name=_("Стать"))
    avatar = models.ImageField(verbose_name=_("Аватарка"), upload_to=upload_location, blank=True,
                               help_text=_("Фото користувача"))
    profile_create = models.DateTimeField(auto_now_add=True, verbose_name=_("Дата створення профіля"))
    profile_update = models.DateTimeField(auto_now=True, verbose_name=_("Дата оновлення профіля"))

    def __str__(self):
        return self.user.get_full_name()




