# organizational_info/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import InternalControl, CorporateGovernance, AccountingProcess
from .forms import InternalControlForm, CorporateGovernanceForm, AccountingProcessForm

def internal_control_list(request):
    internal_controls = InternalControl.objects.all()
    return render(request, 'organizational_info/internal_control_list.html', {'internal_controls': internal_controls})

def internal_control_detail(request, pk):
    internal_control = get_object_or_404(InternalControl, pk=pk)
    return render(request, 'organizational_info/internal_control_detail.html', {'internal_control': internal_control})

def internal_control_new(request):
    if request.method == "POST":
        form = InternalControlForm(request.POST)
        if form.is_valid():
            internal_control = form.save(commit=False)
            internal_control.save()
            return redirect('organizational_info:internal_control_list')
    else:
        form = InternalControlForm()
    return render(request, 'organizational_info/internal_control_edit.html', {'form': form})

def internal_control_edit(request, pk):
    internal_control = get_object_or_404(InternalControl, pk=pk)
    if request.method == "POST":
        form = InternalControlForm(request.POST, instance=internal_control)
        if form.is_valid():
            internal_control = form.save(commit=False)
            internal_control.save()
            return redirect('organizational_info:internal_control_detail', pk=internal_control.pk)
    else:
        form = InternalControlForm(instance=internal_control)
    return render(request, 'organizational_info/internal_control_edit.html', {'form': form, 'internal_control': internal_control})

def internal_control_delete(request, pk):
    internal_control = get_object_or_404(InternalControl, pk=pk)
    internal_control.delete()
    return redirect('organizational_info:internal_control_list')

# Repeat similar views for Corporate Governance and Accounting Process
