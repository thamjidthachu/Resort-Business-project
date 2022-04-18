from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'service'
urlpatterns = [
    path('', views.PageList.as_view(), name='lists'),
    path('<int:pk>', views.Details.as_view(), name='data'),
    path('abc', views.EndlessView.as_view(), name='services'),
    path('abcd', views.EndlessScrollView.as_view(), name='serve'),
]
