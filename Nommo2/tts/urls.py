from django.urls import path
from tts import views # changed from "." to tts 
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.home, name=""),
    path('register', views.register, name="register"),
    path('my-login', views.my_login, name='my-login'),
    path('logout', views.user_logout, name='logout'),

    #file converter
    path('request', views.request, name = "request"),
    path('dashboard', views.dashboard, name= "dashboard")
]  

if settings.DEBUG:  # Only add this in development - DEBUG = True in settings.py
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)