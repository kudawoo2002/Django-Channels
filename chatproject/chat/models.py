from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Message(models.Model):
    from_who = models.ForeignKey(User, on_delete=models.PROTECT, default=None, related_name="from_user")
    to_who = models.ForeignKey(User, on_delete=models.PROTECT, default=None, related_name="to_user")
    message = models.TextField()
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    has_been_seen = models.BooleanField(null=True, default=False)

    def __str__(self):
        return f"{self.message} [ chat message From  {self.from_who.first_name} {self.from_who.last_name} To {self.to_who.first_name} {self.to_who.last_name}]"
    



class UserChannel(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, default=None)
    channel_name = models.TextField()

   