from django.db import models

class Subscriber(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return "Пользователь: %s Эл.Почта: %s" % (self.name, self.email)

    class Meta:
        verbose_name = 'My Subscriber'
        verbose_name_plural = 'A lot of Subscribers'
