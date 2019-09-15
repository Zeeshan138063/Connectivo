from django.db import models
# Create your models here.


class Log(models.Model):
    is_uploaded = models.BooleanField(default=False)
    is_new = models.BooleanField(default=False)

    class Meta:
        abstract = True


class Account(models.Model):
    account_code = models.CharField(max_length=128)
    username = models.CharField(max_length=128, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    first_name = models.CharField(max_length=128, blank=True, null=True)
    last_name = models.CharField(max_length=128, blank=True, null=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    has_live_subscription = models.BooleanField(default=False)
    has_active_subscription = models.BooleanField(default=False)


class Invoice(Log):
    account_code = models.ForeignKey(Account, models.SET_NULL,
                                     blank=True,
                                     null=True, )
    uuid = models.CharField(max_length=150)
    username = models.CharField(max_length=128, blank=True, null=True)
    state = models.CharField(max_length=20)
    invoice_number = models.CharField(max_length=100)


class Subscription(Log):
    account_code = models.ForeignKey(Account, models.SET_NULL,
                                     related_name='user_subscription',
                                     blank=True,
                                     null=True, )
    uuid = models.CharField(max_length=150)
    plan_code = models.CharField(max_length=150)
    state = models.CharField(max_length=20)
    quantity = models.IntegerField(default=1)


class Plan(models.Model):
    subscription = models.OneToOneField(Subscription,
                                     related_name='subscription_plan',
                                     on_delete=models.SET_NULL,
                                     blank=True,
                                     null=True, )
    uuid = models.CharField(max_length=150)
    plan_code = models.CharField(max_length=150)
    state = models.CharField(max_length=20)
    name = models.CharField(max_length=256)
