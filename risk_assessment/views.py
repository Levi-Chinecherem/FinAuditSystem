# risk_assessment/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import RiskAssessment
from .forms import RiskAssessmentForm

@login_required
def risk_assessment_list(request):
    risk_assessments = RiskAssessment.objects.filter(user=request.user)
    return render(request, 'risk_assessment/risk_assessment_list.html', {'risk_assessments': risk_assessments})

@login_required
def risk_assessment_detail(request, pk):
    risk_assessment = RiskAssessment.objects.get(pk=pk)
    return render(request, 'risk_assessment/risk_assessment_detail.html', {'risk_assessment': risk_assessment})

@login_required
def risk_assessment_create(request):
    if request.method == 'POST':
        form = RiskAssessmentForm(request.POST)
        if form.is_valid():
            risk_assessment = form.save(commit=False)
            risk_assessment.user = request.user
            risk_assessment.save()
            return redirect('risk_assessment:risk_assessment_list')
    else:
        form = RiskAssessmentForm()
    return render(request, 'risk_assessment/risk_assessment_form.html', {'form': form})

@login_required
def risk_assessment_update(request, pk):
    risk_assessment = RiskAssessment.objects.get(pk=pk)
    if request.method == 'POST':
        form = RiskAssessmentForm(request.POST, instance=risk_assessment)
        if form.is_valid():
            form.save()
            return redirect('risk_assessment:risk_assessment_list')
    else:
        form = RiskAssessmentForm(instance=risk_assessment)
    return render(request, 'risk_assessment/risk_assessment_form.html', {'form': form})

@login_required
def risk_assessment_delete(request, pk):
    risk_assessment = RiskAssessment.objects.get(pk=pk)
    risk_assessment.delete()
    return redirect('risk_assessment:risk_assessment_list')
