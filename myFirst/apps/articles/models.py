from django.db import models
import datetime
from django.utils import timezone


class Article(models.Model):
    article_title = models.CharField("article's title", max_length=250)
    article_text = models.TextField("article's text")
    pub_date = models.DateTimeField("publish date")

    def __str__(self):
        return self.article_title

    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days=7))

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author_name = models.CharField("author's name", max_length=30)
    comment_text = models.CharField("comment text", max_length=250)

    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'
