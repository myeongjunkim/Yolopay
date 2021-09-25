from django.db import models

# Create your models here.
class Yolopay(models.Model):
    seq = models.AutoField(primary_key=True)
    body = models.TextField()
    emotion = models.CharField(max_length=50)
    yolo_fire = models.CharField(max_length=50)
    date = models.CharField(max_length=50)

    def __str__(self):
        return self.body[:10]
    