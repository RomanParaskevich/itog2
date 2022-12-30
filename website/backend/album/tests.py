from django.test import TestCase, Client
from .models import Album, Photo, Tag
from user.models import User
from django.contrib.auth.hashers import make_password


class AlbumTestCase(TestCase):
    def setUp(self):
        u1 = User.objects.create(username='User1', password=make_password('password1'), email='email1@mail.ru', is_active=True)
        u2 = User.objects.create(username='User2', password=make_password('password2'), email='email2@mail.ru', is_active=True)
        a1 = Album.objects.create(name='Album1', user=u1)
        a2 = Album.objects.create(name='Album1', user=u1)
        a3 = Album.objects.create(name='Album2', user=u2)
        t1 = Tag.objects.create(name='tag1')
        t2 = Tag.objects.create(name='tag2')
        Photo.objects.create(title='photo1', img='img1.jpg', img_height=1800, img_width=1200, album=a1).tags.set([])
        Photo.objects.create(title='photo2', img='img2.png', img_height=1800, img_width=1200, album=a1).tags.set([t1, t2])
        Photo.objects.create(title='photo3', img='img3.jpg', img_height=1800, img_width=1200, album=a2).tags.set([])
        Photo.objects.create(title='photo4', img='img4.jpg', img_height=1800, img_width=1200, album=a3).tags.set([t1])

    def test_create_album(self):
        albums_number = len(Album.objects.all())
        u1 = User.objects.get(username='User1')
        Album.objects.create(name='Album', user=u1)
        self.assertEqual(len(Album.objects.all()), albums_number + 1)

    def test_user_login(self):
        c = Client()
        response = c.post('/api/v1/auth/login/', {'username': 'User1', 'password': 'password1'})
        self.assertEqual(response.status_code, 302)

    def test_get_albums_api_status(self):
        c = Client()
        c.login(username='User1', password='password1')
        response = c.get('/api/v1/albums/albums/')
        self.assertEqual(response.status_code, 200)

    def test_post_albums_api(self):
        c = Client()
        c.login(username='User1', password='password1')
        response = c.post('/api/v1/albums/albums/', {'name': 'Album4'})
        self.assertEqual(response.status_code, 201)

    def test_get_photos_api_status(self):
        c = Client()
        c.login(username='User1', password='password1')
        response = c.get('/api/v1/albums/photos/')
        self.assertEqual(response.status_code, 200)

    def test_post_albums_api_unauthorised_user(self):
        c = Client()
        response = c.post('/api/v1/albums/albums/', {'name': 'Album4'})
        self.assertEqual(response.status_code, 401)
