from django.db import models

# Create your models here.
from django.db import models

class Term(models.Model):
    type = models.CharField(max_length=50)  # 대분류
    terms = models.CharField(max_length=100)  # 용어 이름
    definition = models.TextField()  # 정의

    def __str__(self):
        return self.terms