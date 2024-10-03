from django.db import models
from accounts.models import CustomUser


class APIRequest(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    method = models.CharField(max_length=10)
    request_time = models.DateTimeField(auto_now_add=True)
    endpoint = models.CharField(max_length=100)
    status_code = models.IntegerField()
    

    def __str__(self):
        if self.user is None:
            return f'Anonymous | {self.method} | {self.endpoint}'
        return f'{self.user.username} | {self.method} | {self.endpoint}'
