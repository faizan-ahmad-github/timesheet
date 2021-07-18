from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import TimeField


class logtime(models.Model):
    user = models.ForeignKey(User,  on_delete=models.CASCADE)
    time = models.TimeField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    class Meta:
        get_latest_by = [""]
