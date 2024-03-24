from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from.models import ChemistryTopic

def chemistry_chapter_view(request):
    chemistry_chapters=ChemistryTopic.objects.all()
    return render(request,'chemistry/chemistry.html',{'chemsitry_chapters':chemistry_chapters})
def chemistry_chapter_detail(request,pk):
    item=get_object_or_404(ChemistryTopic,pk=pk)
    return render(request, 'chemistry/chemistry_detail.html', {'item':item})

