# organizational_info/models.py
from django.db import models

class InternalControl(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class CorporateGovernance(models.Model):
    policy_name = models.CharField(max_length=255)
    details = models.TextField()

    def __str__(self):
        return self.policy_name

class AccountingProcess(models.Model):
    process_name = models.CharField(max_length=255)
    details = models.TextField()

    def __str__(self):
        return self.process_name
