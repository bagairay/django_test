#path('hello/',include('hello.urls'))

from django.urls import path
from.import views

urlpatterns=[
    path('',views.index,name='index'), #views.pyのindexを呼ぶ
    path('create', views.create,name='create'),
   # path('test',views.test,name='test'),
   # path('form' , views.form, name='form'),
]