import uuid

from django.contrib.auth.models import User
from django.db import models


class Skill( models.Model ):    # verbose_name="ОПЦИИ"
    name = models.CharField( max_length=50, blank=True, null=True )
    #slug = models.SlugField()
    slug = models.SlugField( unique=True )
    description = models.TextField( null=True, blank=True )
    created = models.DateTimeField( auto_now_add=True )
    id = models.UUIDField( default=uuid.uuid4, unique=True,
                           primary_key=True, editable=False )

    def __str__(self):
        return str( self.name )


class Profile( models.Model ):  #, verbose_name="ПОСТАВЩИКИ"
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True )
    name = models.CharField( max_length=50, blank=True, null=True )
    email = models.EmailField( max_length=50, blank=True, null=True )
    username = models.CharField( max_length=50, blank=True, null=True )
    city = models.CharField( max_length=50, blank=True, null=True, verbose_name="город" )
    intro = models.CharField( max_length=200, blank=True, null=True )
    bio = models.TextField( blank=True, null=True )
    image = models.ImageField(
        null=True, blank=True, upload_to='profile_images/', default="profile_images/default.jpg",
        verbose_name='Изображение' )
    skills = models.ManyToManyField( Skill, blank=True )
    github = models.CharField( max_length=100, blank=True, null=True )
    twitter = models.CharField( max_length=100, blank=True, null=True )
    linkedin = models.CharField( max_length=100, blank=True, null=True )
    youtube = models.CharField( max_length=100, blank=True, null=True )
    website = models.CharField( max_length=100, blank=True, null=True )
    created = models.DateTimeField( auto_now_add=True )
    id = models.UUIDField( default=uuid.uuid4, unique=True,
                           primary_key=True, editable=False )

    def __str__(self):
        return str( self.username )

    class Meta:
        ordering = ['created']


class Message( models.Model):   # , verbose_name="СООБЩЕНИЯ"
    sender = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, null=True, blank=True )
    recipient = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, null=True, blank=True, related_name="messages" )
    name = models.CharField( max_length=200, null=True, blank=True, verbose_name="Имя" )
    email = models.EmailField( max_length=200, null=True, blank=True, verbose_name="Электронная почта" )
    subject = models.CharField( max_length=200, null=True, blank=True, verbose_name="Кому" )
    body = models.TextField( verbose_name="Текст сообщения")
    is_read = models.BooleanField( default=False, null=True )
    created = models.DateTimeField( auto_now_add=True )
    id = models.UUIDField( default=uuid.uuid4, unique=True,
                           primary_key=True, editable=False )

    def __str__(self):
        return self.subject

    class Meta:
        ordering = ['is_read', '-created']
