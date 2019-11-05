from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_of_day, name='NewsToday'),
    path('archives/(\d{4}-\d{2}-\d{2})/',views.past_days_news,name='pastNews'),
    path('search/', views.search_results, name='search_results')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)