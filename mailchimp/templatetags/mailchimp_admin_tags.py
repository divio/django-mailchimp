from django import template

register = template.Library()

@register.filter
def can_dequeue(user, obj):
    return obj.can_dequeue(user)
