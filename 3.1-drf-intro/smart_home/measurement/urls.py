from django.urls import path

from measurement.views import SensorsView, SensorDetailView, MeasurementView

urlpatterns = [
    path('sensors/', SensorsView.as_view(), name='list_sensors'),
    path('sensors/<int:pk>/', SensorDetailView.as_view(), name='sensor'),
    path('measurements/', MeasurementView.as_view(), name='create_measurement'),
]
