from django.db import models

class Comments(models.Model):
    text = models.TextField("Комментарий")
    created = models.DateTimeField("Дата добавления", auto_now_add=True, null=True)



    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = 'Коментарии'

    def __str__(self):
        return self.created