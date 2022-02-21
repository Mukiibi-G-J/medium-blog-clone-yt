from django.urls import path
from .views import list_view, detail_view

app_name = 'blog'

urlpatterns = [
    path( '', list_view, name='list_view'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', detail_view, name='detail_view')
]