from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path('',views.chemistry_chapter_view,name="chemistry_chapters"),
    path('<int:pk>/',views.chemistry_chapter_detail,name="chemistry_detail")


] +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)