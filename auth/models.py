from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone
class Owner(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ('created',)


class Collaborator(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ('created',)


class Reader(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ('created',)


class GithubUser(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    access_token = models.CharField()
    refresh_token = models.CharField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ('created',)


@receiver(post_save, sender=User)
def create_user_roles(sender, instance, created, **kwargs):
    """
    Creates an associated Owner, Collaborator, Reader, and GithubUser profile (role) for each created User.
    :param sender: User model
    :param instance: User instance
    :param created: Boolean (TODO check this)
    :param kwargs: (TODO check what the kwargs might be)
    :return:
    """
    if created:
        Owner.objects.create(user=instance)
        Collaborator.objects.create(user=instance)
        Reader.objects.create(user=instance)
        GithubUser.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_roles(sender, instance, **kwargs):
    """
    Updates associated Owner, Collaborator, Reader, and GithubUser roles a User instance when a User instance is saved.
    :param sender:
    :param instance:
    :param kwargs:
    :return:
    """
    instance.owner.save()
    instance.collaborator.save()
    instance.reader.save()
