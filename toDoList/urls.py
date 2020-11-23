from django.urls import path
from . import views

# URLs are resolved from here
urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.addToDoItem, name='add'),
    path('completed/<todo_id>', views.completedToDo, name='completed'),
    path('deleteCompleted', views.deleteCompleted, name='deleteCompleted'),
    path('deleteAll', views.deleteAll, name='deleteAll'),
]
