from django.urls import path
from . import views

app_name = 'service'
urlpatterns = [
    path('', views.PageList.as_view(), name='lists'),
    path('endless', views.EndlessScroll.as_view(), name='infinity'),
    path('reply', views.replyPost, name='replies'),
    path('<slug:slug>', views.Details.as_view(), name='datas'),
]
