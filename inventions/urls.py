from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('list', views.list, name='list'),
    path('inventions/', views.InventionListView.as_view(), name='inventions'),
    path('inventions/categories/<str:category_name>/', views.InventionListView.as_view(), name='invention_category'),
    path('inventions/<int:pk>/', views.InventionDetailView.as_view(), name='invention_detail'),
    path('inventions/<int:pk>/', views.InventionDetailView.as_view(), name='invention-detail'),

    path('inventions/create/', views.InventionCreate.as_view(), name='invention-create'),
    path('inventions/<int:pk>/update/', views.InventionUpdate.as_view(), name='invention-update'),
    path('inventions/<int:pk>/delete/', views.InventionDelete.as_view(), name='invention-delete'),
    # path('inventions/<int:pk>/edit/', views.edit_invention, name='invention-edit'),

    path('inventions/statistics/', views.statistics, name='statistics'),
]
