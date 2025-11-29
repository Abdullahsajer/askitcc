from django.shortcuts import render, redirect, get_object_or_404
from .models import TransportTask
from .forms import TransportForm

# قائمة مهام النقل
def transport_list_view(request):
    tasks = TransportTask.objects.all().order_by("-id")
    return render(request, "transport/transport_list.html", {"tasks": tasks})

# إضافة مهمة
def add_transport_view(request):
    if request.method == "POST":
        form = TransportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/transport/")
    else:
        form = TransportForm()

    return render(request, "transport/add_transport.html", {"form": form})

# تعديل مهمة
def edit_transport_view(request, task_id):
    task = get_object_or_404(TransportTask, id=task_id)

    if request.method == "POST":
        form = TransportForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("/transport/")
    else:
        form = TransportForm(instance=task)

    return render(request, "transport/edit_transport.html", {"form": form, "task": task})

# حذف مهمة
def delete_transport_view(request, task_id):
    task = get_object_or_404(TransportTask, id=task_id)
    task.delete()
    return redirect("/transport/")
