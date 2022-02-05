from django.urls import path
from .views import zipView,cityView,citydataView,zipdataView,updateView,deleteView



urlpatterns =[

    path('', cityView, name='cityview'),
    path('zip/', zipView, name = 'zipview'),
    path('citydata/',citydataView, name = 'citydata' ),
    path('zipdata/', zipdataView, name = 'zipdata' ),
    path('update/<str:id>/', updateView, name='updateview'),
    path('delete/<str:id>/', deleteView, name='deleteview')

]