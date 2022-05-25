from django.db import models


class Article(models.Model):
    article_title = models.CharField("article's title", max_length=250)
