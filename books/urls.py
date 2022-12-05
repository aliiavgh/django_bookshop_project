from django.urls import path
from .views import BookListCreateApiView, BookRetrieveUpdateApiView, BookDestroyApiView

urlpatterns = [
    path('', BookListCreateApiView.as_view()),
    path('<int:pk>/', BookRetrieveUpdateApiView.as_view()),
    path('del/<int:pk>/', BookDestroyApiView.as_view())
]