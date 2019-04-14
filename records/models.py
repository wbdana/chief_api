from django.db import models


class Record(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    language = models.CharField(max_length=50, blank=True, default='python')
    owner = models.ForeignKey('auth.User', related_name='records', on_delete=models.CASCADE)

    class Meta:
        ordering = ('created',)

