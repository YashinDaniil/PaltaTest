from django.urls import path
from .views import SetPosition, RevokeTask, GetOldSearch

urlpatterns = [
    path('set_position/', SetPosition.as_view()),
    path('revoke_task', RevokeTask.as_view()),
    path('get_old_search/<uuid:user_id>', GetOldSearch.as_view()),
]