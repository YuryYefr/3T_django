from django.urls import  path
from . import views
from .views import TrackerList, TrackerDetail, TrackerCreate, TrackerUpdate
urlpatterns = [
    path('', TrackerList.as_view(), name='trackers-home'),
    path('tracker/<int:pk>/', TrackerDetail.as_view(), name='tracker-detail'),
    path('tracker/new/', TrackerCreate.as_view(), name='tracker-create'),
    path('tracker/<int:pk>/update/', TrackerUpdate.as_view(), name='tracker-update'),
    path('about/', views.about, name='trackers-about'),
]