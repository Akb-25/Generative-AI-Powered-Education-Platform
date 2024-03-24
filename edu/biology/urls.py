from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path('',views.biology_chapter_view,name="biology_chapters"),
    path('<int:pk>/',views.biology_chapter_detail,name="biology_detail")
    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
# urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)