from django.db import models


class Article(models.Model):
    article_title = models.CharField("article's title", max_length=250)
    article_text = models.TextField("article's text")
    pub_date = models.DateTimeField("publish date")


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author_name = models.CharField("author's name", max_length=30)
    comment_text = models.CharField("comment text", max_length=250)
