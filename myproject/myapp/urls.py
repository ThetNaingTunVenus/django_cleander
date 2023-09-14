from django.urls import path
from .views import *
from . import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', include('myapp.urls')),
    path('', views.index, name='index'),
    path('all_events/', views.all_events, name='all_events'), 
    path('add_event/', views.add_event, name='add_event'), 
    path('update/', views.update, name='update'),
    path('remove/', views.remove, name='remove'),
]