



from django.urls import path
from .import views

urlpatterns = [
    path('',views.inicio,name='inicio'),
    path('sha1',views.sha1,name='sha1'),
    path('sha256',views.sha256,name='sha256')
]