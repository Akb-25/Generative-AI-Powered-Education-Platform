from django.contrib import admin
from django.urls import path,include
from core.views import home
from django.conf import settings
from django.conf.urls.static import static
from login import views as v
urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('accounts/',include("django.contrib.auth.urls")),
    # path('login/',v.login,name='login'),
    # path('register/',v.register,name='register'),
    # path('',home,name='home'),
    path('admin/',admin.site.urls),
    path('',include('core.urls')),
]