from django.db import models
from django.utils import timezone


class Post(models.Model):
    #작성자
    author = models.ForeignKey('auth.User')
    #제목
    title = models.CharField(max_length=200)
    #내용
    text = models.TextField()
    #생성일자
    created_date = models.DateTimeField(default=timezone.now)
    #게시일자
    published_date = models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return self.title

    def publish(self):
        self.published_date = timezone.now()
        self.save()