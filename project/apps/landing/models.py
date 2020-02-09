from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class ContactForm(models.Model):
    messages = models.TextField(max_length=2000, blank=True, null=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    open_date = models.DateTimeField(auto_now_add=True)
    sending_date = models.DateTimeField()


class ContactItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    sending = models.BooleanField(default=False)
    form = models.ForeignKey(ContactForm, on_delete=models.CASCADE)


class Contact(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    items = models.ManyToManyField(ContactItem)
    answered = models.BooleanField(default=False)

    contact_form_object_id = models.IntegerField(
        blank=True,
        null=True,
    )

    contact_form_content_type = models.ForeignKey(
        ContentType,
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )

    contact_form = GenericForeignKey(
        'contact_form_content_type',
        'contact_form_object_id',
    )
