from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [

    path('basic-splitting',views.Basic_Splitting,name="Basic_Splitting" ),
    path('bill-splitting',views.Bill_Splitting,name="Bill_Splitting" ),
    path('unevenly-splitting',views.split_unevenly,name="split_unevenly" ),
    path('split-including-tip-tax',views.Tip_And_Tax,name="Tip_And_Tax" ),
    path('split-with-discount',views.Discount,name="Discount" ),

]
