from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('create', views.create),
    path('add', views.add),
    path('edit/<int:user_id>', views.edit),
    path('update/<int:user_id>', views.update),
    path('show/<int:user_id>', views.show),
    path('delete/<int:user_id>', views.delete)
]