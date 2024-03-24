from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path('',views.home,name=""),
    path('register/',views.register,name="register"),
    path('login/',views.login,name="login"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('logout/',views.logout,name="logout"),
    path('chemistry/',include('chemistry.urls')),
    path('biology/',include('biology.urls')),
    path('physics/',include('physics.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)