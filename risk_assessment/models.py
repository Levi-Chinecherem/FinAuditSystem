# risk_assessment/models.py
from django.db import models
from django.contrib.auth.models import User

class RiskAssessment(models.Model):
    RISK_CATEGORIES = [
        ('FINANCIAL', 'Financial Risk'),
        ('OPERATIONAL', 'Operational Risk'),
        ('COMPLIANCE', 'Compliance Risk'),
        ('STRATEGIC', 'Strategic Risk'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=20, choices=RISK_CATEGORIES)
    description = models.TextField()
    impact = models.CharField(max_length=255)
    likelihood = models.CharField(max_length=255)
    mitigation_plan = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.category} Risk Assessment at {self.timestamp}"
