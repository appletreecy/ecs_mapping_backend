from django.urls import path
from .views import GetECSMappingView

urlpatterns = [
    path('mappings/ecs/', GetECSMappingView.as_view(), name='get-ecs-mapping'),
]