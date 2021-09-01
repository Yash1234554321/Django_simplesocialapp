from django.db import models
from django.utils.text import slugify
from django.urls import reverse

from django.contrib.auth import get_user_model
User = get_user_model()# it connects to the models of account meaning the user that is logged in

from django import template
register = template.Library()

class Group(models.Model):
    name = models.CharField(max_length=255,unique=True)
    slug = models.SlugField(allow_unicode=True,unique=True)
    description = models.TextField(blank=True,default='')
    description_html = models.TextField(editable=False,default='',blank=True)
    members = models.ManyToManyField(User,through='GroupMember')

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)#slug will help when we enter space in between names
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('groups:single',kwargs={'slug':self.slug})

    class Meta:
        ordering = ['name']

class GroupMember(models.Model):
    group = models.ForeignKey(Group,related_name='memberships',on_delete=models.CASCADE)# related name means groupmember will be realted with group class by that name
    user = models.ForeignKey(User,related_name='user_groups',on_delete=models.CASCADE)#User that is currently logged in

    def __str__(self):
        self.user.username

    class Meta:
        unique_together = ('group','user')
