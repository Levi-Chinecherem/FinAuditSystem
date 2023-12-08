from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import AuditLog
from .forms import AuditLogForm
from django.http import HttpRequest
# Import the get_client_ip function
from .utils import get_client_ip

@login_required
def audit_log(request):
    audit_logs = AuditLog.objects.filter(user=request.user).order_by('-timestamp')
    form = AuditLogForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.instance.user = request.user
        form.save()
        return redirect('audit:audit_log')

    context = {'audit_logs': audit_logs, 'form': form}
    return render(request, 'audit/audit_log.html', context)

@login_required
def audit_log_list(request):
    audit_logs = AuditLog.objects.filter(user=request.user).order_by('-timestamp')
    return render(request, 'audit/audit_log_list.html', {'audit_logs': audit_logs})

@login_required
def audit_log_detail(request, audit_log_id):
    audit_log = get_object_or_404(AuditLog, id=audit_log_id, user=request.user)
    return render(request, 'audit/audit_log_detail.html', {'audit_log': audit_log})

@login_required
def audit_log_create(request):
    if request.method == 'POST':
        form = AuditLogForm(request.POST)
        if form.is_valid():
            # Set the user and source_ip using the request object
            form.instance.user = request.user
            form.instance.source_ip = get_client_ip(request)
            form.save()
            return redirect('audit:audit_log_list')
    else:
        form = AuditLogForm()

    return render(request, 'audit/audit_log_form.html', {'form': form, 'action': 'Create'})

@login_required
def audit_log_update(request, audit_log_id):
    audit_log = get_object_or_404(AuditLog, id=audit_log_id, user=request.user)

    if request.method == 'POST':
        form = AuditLogForm(request.POST, instance=audit_log)
        if form.is_valid():
            form.instance.source_ip = get_client_ip(request)
            form.save()
            return redirect('audit:audit_log_list')
    else:
        form = AuditLogForm(instance=audit_log)

    return render(request, 'audit/audit_log_form.html', {'form': form, 'action': 'Update'})

@login_required
def audit_log_delete(request, audit_log_id):
    audit_log = get_object_or_404(AuditLog, id=audit_log_id, user=request.user)

    if request.method == 'POST':
        audit_log.delete()
        return redirect('audit:audit_log_list')

    return render(request, 'audit/audit_log_confirm_delete.html', {'audit_log': audit_log})
