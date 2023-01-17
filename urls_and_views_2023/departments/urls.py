from django.urls import path

from urls_and_views_2023.departments.views import sample_view

urlpatterns = (
    path('', sample_view),
    path('<department_id>/', sample_view),
    path('int/<int:department_id>/', sample_view),
)
