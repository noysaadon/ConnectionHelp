from django import views
from django.urls import path
from volnteer import views

urlpatterns = [
    path('volnteer_charity/', views.choose_volnteer_charity , name='volnteer_charity'),
    path('volnteers/', views.volnteer , name='volnteers'),
    path('volnteers/vol_child', views.filter_volnteer_child, name='vol_child'),
    path('volnteer/vol_singleparent', views.filter_volnteer_singleparent, name='vol_singleparent'),
    path('volnteer/vol_elders', views.filter_volnteer_elders, name='vol_elders'),
    path('charities/', views.charities, name='charities' ),
    path('charities/char_child', views.filter_charity_child, name='char_child' ),
    path('charities/char_singleparent', views.filter_charity_singleparent, name='char_singleparent'),
    path('charities/char_elders', views.filter_charity_elders, name='char_elders'),
]
