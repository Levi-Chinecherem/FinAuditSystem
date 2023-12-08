from django.db import models
from django.contrib.auth.models import User

class AuditLog(models.Model):
    AUDIT_ACTIONS = [
    ('AUTOMATED_AUDIT', 'Automated Audit'),
    ('DATA_CLASSIFICATION', 'Data Classification'),
    ('TPA_REGULAR_CHECK', 'TPA Regular Check'),
    ('DYNAMIC_DATA_OPERATION', 'Dynamic Data Operation'),
    ('RISK_ASSESSMENT', 'Risk Assessment'),
    ('USER_COLLABORATION', 'User Collaboration'),
    ('INFO_MANAGEMENT', 'Information Management'),
    ('SYSTEM_EFFICIENCY', 'System Efficiency'),
    ('COMPLIANCE_CHECK', 'Compliance Check'),
    ('SECURITY_INCIDENT', 'Security Incident Investigation'),
    ('DATA_BACKUP_RESTORE', 'Data Backup and Restore'),
    ('ACCESS_GRANT_REVOKE', 'Access Grant/Revoke'),
    ('AUDIT_REPORT_GENERATION', 'Audit Report Generation'),
    ('SYSTEM_UPGRADE', 'System Upgrade'),
    ('EXTERNAL_SYSTEM_INTEGRATION', 'External System Integration'),
]

    RELATED_OBJECTS = [
    ('USER_ACCOUNT', 'User Account'),
    ('FINANCIAL_TRANSACTION', 'Financial Transaction'),
    ('DATA_RECORD', 'Data Record'),
    ('DATABASE_TABLE', 'Database Table'),
    ('SYSTEM_SETTING', 'System Setting'),
    ('DOCUMENT', 'Document'),
    ('SECURITY_POLICY', 'Security Policy'),
    ('APPLICATION', 'Application'),
    ('NETWORK_DEVICE', 'Network Device'),
    ('EMPLOYEE_RECORD', 'Employee Record'),
    ('VENDOR_CONTRACT', 'Vendor Contract'),
    ('CLIENT_RECORD', 'Client Record'),
    ('PROJECT', 'Project'),
    ('SERVICE_REQUEST', 'Service Request'),
    ('AUDIT_LOG_ENTRY', 'Audit Log Entry'),
]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=50, choices=AUDIT_ACTIONS)
    description = models.TextField(blank=True, null=True)
    source_ip = models.GenericIPAddressField(blank=True, null=True)
    related_object = models.CharField(max_length=50, choices=RELATED_OBJECTS)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.get_action_display()} at {self.timestamp}"
