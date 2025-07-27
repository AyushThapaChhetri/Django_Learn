from django.urls import path
from . import views
from .views import BookListView, BookCreateView, BookDeleteView, BookUpdateView

urlpatterns = [
    path('hello', views.hello),
    path('', BookListView.as_view(), name='book_list'),
    path('create/', BookCreateView.as_view(),name='book_create'),
    path('update/<uuid>', BookUpdateView.as_view(),name='book_update'),
    path('delete/<uuid>', BookDeleteView.as_view(), name='book_delete'),
]