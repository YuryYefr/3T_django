from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import TrackerList, TrackerDetail, TrackerCreate, TrackerUpdate, UserTrackerlistView
urlpatterns = [
    path('', TrackerList.as_view(), name='trackers-home'),
    path('user/<str:user_name>', UserTrackerlistView.as_view, name='user-trackers'),
    path('tracker/<int:pk>/', TrackerDetail.as_view(), name='tracker-detail'),
    path('tracker/new/', TrackerCreate.as_view(), name='tracker-create'),
    path('tracker/<int:pk>/update/', TrackerUpdate.as_view(), name='tracker-update'),
    path('about/', views.about, name='trackers-about'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)