from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.template.loader import render_to_string
from accounts.models import CustomUser
from .fields import OrderField

# Create your models here.
class Subject(models.Model):
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    instructor = models.ForeignKey(CustomUser, related_name='instructor', limit_choices_to={'is_instructor': True}, blank=True, null=True, on_delete=models.SET_NULL)
    
    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
    
class Course(models.Model):

    owner = models.ForeignKey(CustomUser, related_name='courses_created', on_delete=models.CASCADE)
    students = models.ManyToManyField(CustomUser, related_name='courses_joined', blank=True)
    subject = models.ForeignKey(Subject, related_name='courses', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    overview = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title
    
class Module(models.Model):

    course = models.ForeignKey(Course, related_name='modules', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    order = OrderField(blank=True, for_fields=['course'])

    def __str__(self):
        return f'{self.order}. {self.title}'

    class Meta:
            ordering = ['order']
    
class Content(models.Model):
    module = models.ForeignKey(Module, related_name='contents', on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, limit_choices_to={'model_in':(
        'text',
        'video',
        'image',
        'file',
    )})
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type', 'object_id')
    order = OrderField(blank=True, for_fields=['module'])

    class Meta:
            ordering = ['order']

class ItemBase(models.Model):
    owner = models.ForeignKey(CustomUser, related_name='%(class)s_related', on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title
    
    def render(self):
        return render_to_string(
            f'courses/content/{self._meta.model_name}.html',
            {'item': self}
        )
    
class Text(ItemBase):
    content = models.TextField()

class File(ItemBase):
    file = models.FileField(upload_to='files')

class Image(ItemBase):
    file = models.FileField(upload_to='images')

class Video(ItemBase):

    url = models.URLField()

class School(models.Model):

    instructors = models.ManyToManyField(CustomUser, related_name='instructors', blank=True)
    students = models.ManyToManyField(CustomUser, related_name='students', blank=True)
    courses = models.ManyToManyField(Course, related_name='courses', blank=True)
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name