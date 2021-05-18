from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Author(models.Model):
    author = models.CharField(max_length=200)
    rating_auth = models.IntegerField(default=0)

    one_to_one_rel = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.author

    def update_rating(self, self.rating_auth):
        sum_rat_post = Post.objects.filter(one_to_many_rel=Author).rating_post * 3
        sum_rat_comm = Comment.objects.filter(one2many_user=User).rating_comm
        sum_rat_auth = Comment.objects.filter(one2many_post=Post, one2many_user=User).rating_auth
        self.rating_auth = sum_rat_post + sum_rat_comm + sum_rat_auth
        self.save()


class Category(models.Model):
    category = models.CharField(max_length=100, unique=True)


class Post(models.Model):
    state = 'ST'
    new = 'NE'
    POSITIONS = [
        (state, 'Статья'),
        (new, 'Новость')
    ]
    st_or_new = models.CharField(max_length=2,
                                 choices=POSITIONS,
                                 default=state)
    created = models.DateTimeField(auto_now_add=True)
    post_name = models.CharField(max_length=250)
    content = models.TextField()
    rating_post = models.IntegerField(default=0)

    one_to_many_rel = models.ForeignKey(Author, on_delete=models.CASCADE)
    many_to_many_rel = models.ManyToManyField(Category, through='PostCategory')

    def like(self):
        self.rating_post += 1
        self.save()

    def dislike(self):
        self.rating_post -= 1
        if self.rating_comm < 0:
            self.rating_comm = 0
        self.save()

    def preview(self):
        prev = self.content[:124] + '...'
        return prev


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    comment = models.TextField()
    created_comm = models.DateTimeField(auto_now_add=True)
    rating_comm = models.IntegerField(default=0)

    one2many_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    one2many_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def like(self):
        self.rating_comm += 1
        self.save()

    def dislike(self):
        self.rating_comm -= 1
        if self.rating_comm < 0:
            self.rating_comm = 0
        self.save()

