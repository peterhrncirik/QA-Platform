from django import template
register = template.Library()

from courses.models import School

@register.filter(name='has_group')
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists()

@register.filter(name='school')
def school(user):

    if user.is_instructor:
        return School.objects.get(instructors=user)
    elif user.is_student:
        return School.objects.get(students=user)