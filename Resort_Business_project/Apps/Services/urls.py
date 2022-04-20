from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'service'
urlpatterns = [
    path('', views.PageList.as_view(), name='lists'),
    path('endless', views.EndlessScroll.as_view(), name='infinity'),
    path('<slug:slug>', views.Details.as_view(), name='data'),
]
