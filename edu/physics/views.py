from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import PhysicsTopic

def physics_chapter_view(request):
    physics_chapters=PhysicsTopic.objects.all()
    return render(request,'physics/physics.html',{'physics_chapters':physics_chapters})
def physics_chapter_detail(request,pk):
    item=get_object_or_404(PhysicsTopic,pk=pk)
    return render(request, 'physics/physics_detail.html', {'item':item})

