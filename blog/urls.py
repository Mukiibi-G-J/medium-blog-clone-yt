from django.urls import path
from .views import list_view, detail_view, share_post, test

app_name = 'blog'

urlpatterns = [
    path( '', list_view, name='list_view'),
    path('test/', test, name="home"),

    path('tag/<slug:tag_slug>/', list_view, name='list_view'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', detail_view, name='detail_view'),
    path('<int:post_id>/share', share_post, name='share_post'),
]