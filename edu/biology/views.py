from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import BiologyTopic,BiologyContent
# Create your views here.

def biology_chapter_view(request):
    biology_chapters=BiologyTopic.objects.all()
    return render(request,'biology/biology.html',{'biology_chapters':biology_chapters})

def biology_chapter_detail(request,pk):
    item=get_object_or_404(BiologyContent,pk=pk)
    return render(request, 'biology/biology_detail.html', {'item':item})

