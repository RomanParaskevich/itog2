from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from album.models.album import Album
from album.models.tag import Tag


class Command(BaseCommand):
    help = 'Set data'

    def handle(self, *args, **kwargs):
        tags = ('Природа', 'Животные', 'Машина', 'Овощи', 'Здание')
        User = get_user_model()
        for i in range(1, 10):
            u = User.objects.create_user(username='user' + str(i), email='', password='123')
            Album.objects.create(name=get_random_string(), user=u)
        for t in tags:
            Tag.objects.create(name=t)
        print('setting data: done')
