from django.urls import path
from . import views # Import views to connect routes to view functions

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  # route for cats index
  path('cats/', views.cat_index, name='cat-index'),
  # new route below
  path('cats/<int:cat_id>/', views.cat_detail, name='cat-detail'),
]
