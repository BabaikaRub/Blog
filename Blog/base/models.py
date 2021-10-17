from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    """Категории"""
    name = models.CharField("Категория", max_length=150)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Post(models.Model):
    """Посты"""
    title = models.CharField("Пост", max_length=150)
    tagline = models.CharField("Tag", max_length=100, default="")
    text = models.TextField("Текст")
    post_category = models.ForeignKey(Category, on_delete=models.SET_NULL, verbose_name="Категория", null=True)
    image = models.ImageField("Изображение", upload_to="images/")
    date_create = models.DateTimeField("Время создания", auto_now_add=True)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"


class Comment(models.Model):
    """Комментарии"""
    comment_post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="Комментарий к посту")
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    text = models.TextField("Текст комментария")
    time_create = models.DateTimeField("Время создания", auto_now_add=True)
    parent = models.ForeignKey("self", on_delete=models.SET_NULL, verbose_name="Родитель", blank=True, null=True)

    def __str__(self):
        return f"{self.comment_user.user} - {self.comment_user}"

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
