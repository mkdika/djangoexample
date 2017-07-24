from django.conf.urls import url
from crud import views

# Create your views here.


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'addnewperson/', views.addNewPerson, name='addnewperson'),
    url(r'deleteperson/(?P<uid>\w+)$', views.deletePerson, name='deleteperson'),
    url(r'editperson/(?P<uid>\w+)$', views.editPerson, name='editperson'),
]
