from django.conf.urls import url
from crud import views

# Create your views here.


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'addnewperson/', views.addNewPerson, name='addnewperson'),
]
