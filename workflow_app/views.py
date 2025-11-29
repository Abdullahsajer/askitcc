from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from accounts_app.decorators import permission_required
from .models import Workflow, WorkflowStep
from .forms import WorkflowForm, WorkflowStepForm


# قائمة العمليات
@login_required
@permission_required("workflow.view_workflow")
def workflow_list_view(request):
    workflows = Workflow.objects.all().order_by("-id")
    return render(request, "workflow/workflow_list.html", {"workflows": workflows})


# إضافة عملية جديدة
@login_required
@permission_required("workflow.add_workflow")
def add_workflow_view(request):
    if request.method == "POST":
        form = WorkflowForm(request.POST)
        if form.is_valid():
            workflow = form.save()
            return redirect(f"/workflow/{workflow.id}/")
    else:
        form = WorkflowForm()

    return render(request, "workflow/add_workflow.html", {"form": form})


# تفاصيل عملية
@login_required
@permission_required("workflow.view_workflow")
def workflow_detail_view(request, workflow_id):
    workflow = get_object_or_404(Workflow, id=workflow_id)
    steps = workflow.steps.all().order_by("timestamp")
    step_form = WorkflowStepForm()

    return render(request, "workflow/workflow_detail.html", {
        "workflow": workflow,
        "steps": steps,
        "step_form": step_form,
    })


# إضافة خطوة
@login_required
@permission_required("workflow.add_workflow")
def add_step_view(request, workflow_id):
    workflow = get_object_or_404(Workflow, id=workflow_id)

    if request.method == "POST":
        form = WorkflowStepForm(request.POST)
        if form.is_valid():
            step = form.save(commit=False)
            step.workflow = workflow
            step.save()
    return redirect(f"/workflow/{workflow.id}/")


# تعديل عملية
@login_required
@permission_required("workflow.edit_workflow")
def edit_workflow_view(request, workflow_id):
    workflow = get_object_or_404(Workflow, id=workflow_id)

    if request.method == "POST":
        form = WorkflowForm(request.POST, instance=workflow)
        if form.is_valid():
            form.save()
            return redirect(f"/workflow/{workflow.id}/")
    else:
        form = WorkflowForm(instance=workflow)

    return render(request, "workflow/edit_workflow.html", {
        "workflow": workflow,
        "form": form
    })


# حذف خطوة
@login_required
@permission_required("workflow.edit_workflow")
def delete_step_view(request, step_id):
    step = get_object_or_404(WorkflowStep, id=step_id)
    workflow_id = step.workflow.id
    step.delete()
    return redirect(f"/workflow/{workflow_id}/")


# حذف عملية
@login_required
@permission_required("workflow.delete_workflow")
def delete_workflow_view(request, workflow_id):
    workflow = get_object_or_404(Workflow, id=workflow_id)
    workflow.delete()
    return redirect("/workflow/")
