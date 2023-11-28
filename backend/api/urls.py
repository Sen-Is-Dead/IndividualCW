from django.urls import path
from .views import my_model_view, my_model_detail_view

# URL patterns for MyModel views
urlpatterns = [
    path('mymodel/', my_model_view, name='mymodel_api'),
    path('mymodel/<int:id>/', my_model_detail_view, name='mymodel_detail_api'),
]
