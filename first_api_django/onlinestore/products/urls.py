from django.urls import path

from .views import producet_list,producet_deatail,manufractures_deatails,active_manufracture

urlpatterns = [
    path('producet/',producet_list,name="producet-list"),
    path('producet/<int:pk>/',producet_deatail,name="producet_deatail"),
    path('producet/manufracture/<int:pk>/',manufractures_deatails,name="manufractures_deatails"),
    path('producet/active_manufracture/',active_manufracture,name="active_manufracture"),
    # path("products/<int:pk>/",producetDeatails.as_view(),name="producet-deatails"),
]
