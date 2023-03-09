
from django.urls import path
from .views import CRUD2


urlpatterns = [

    path('persona2/<int:id>',CRUD2.as_view(),name='crud2'),
    path('persona2',CRUD2.as_view(),name='crud2'),
    
]