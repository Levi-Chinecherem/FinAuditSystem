from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from audit.models import AuditLog
from organizational_info.models import InternalControl
from risk_assessment.models import RiskAssessment

# Update your dashboard view
import random

def index(request):
    """Render the index page."""
    return render(request, 'core/index.html')

def dashboard(request):
    # Chart 1: Bar Chart (Example: Number of Audit Logs per Action)
    audit_actions = [action[1] for action in AuditLog.AUDIT_ACTIONS]
    audit_counts = [AuditLog.objects.filter(action=action[0]).count() for action in AuditLog.AUDIT_ACTIONS]

    # Chart 2: Doughnut Chart (Example: Distribution of Internal Controls)
    internal_controls = InternalControl.objects.count()

    # Chart 3: Line Chart (Example: Timeline of Risk Assessments)
    risk_assessments = RiskAssessment.objects.order_by('timestamp')
    risk_dates = [str(assessment.timestamp.date()) for assessment in risk_assessments]
    
    # Generate random values for the line chart based on the total count of risks
    total_risks = RiskAssessment.objects.count()
    risk_counts = [random.randint(0, total_risks) for _ in range(len(risk_dates))]

    # Chart 4: Scatter Plot (Example: Impact vs. Likelihood)
    scatter_data = [{'x': random.uniform(0, 100), 'y': random.uniform(0, 100)} for _ in range(10)]

    context = {
        'audit_actions': audit_actions,
        'audit_counts': audit_counts,
        'internal_controls': internal_controls,
        'risk_dates': risk_dates,
        'risk_counts': risk_counts,
        'scatter_data': scatter_data,
    }

    return render(request, 'core/dashboard.html', context)
