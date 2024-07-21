from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)

    # To change the string representation, we have to define the __str__() function of the Member Model in models.py
    def __str__(self):
        return f"{self.firstname} {self.lastname}"

    
class Comment(models.Model):
    name = models.CharField(_('name'), max_length=64)
    email_address = models.EmailField(_('email address'))
    homepage = models.URLField(_('home page'), blank=True, verify_exists=False)
    comment = models.TextField(_('comment'))
    pub_date = models.DateTimeField(_('published date'), editable=False, auto_now_add=True)
    is_spam = models.BooleanField(_('spam?'), default=False, editable=False)

    class Meta:
        verbose_name = _('comment')
        verbose_name_plural = (_('comments'))