# Create your tasks here
from core.models import Tag, User

from celery import shared_task

@shared_task
def add(x, y):
    print('x, y', x, y)
    user = User.objects.first()
    Tag.objects.create(name='tag1', user=user)
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


# @shared_task
# def count_widgets():
#     return Widget.objects.count()


# @shared_task
# def rename_widget(widget_id, name):
#     w = Widget.objects.get(id=widget_id)
#     w.name = name
#     w.save()