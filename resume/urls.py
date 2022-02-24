
from django.urls import path,include
from resume.views import index_view,contact_view
from django.contrib import admin

app_name = 'resume'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index_view,name='index'),
    path('contact',contact_view,name ='contact'),
]
