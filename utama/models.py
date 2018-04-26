from django.db import models

class Tbl_user(models.Model):
    id_user = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.TextField()

    def __str__(self,):
        return self.id_user
