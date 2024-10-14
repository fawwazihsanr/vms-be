from django.urls import path

from vms.visitor.views import VisitorView, VisitorChartView, DestinationView, BackupDatabaseView

urlpatterns = [
    path('visitor', VisitorView.as_view(), name='visitor_list'),
    path('visitor/<int:visitor_id>', VisitorView.as_view(), name='visitor_detail'),
    path('visitor-chart', VisitorChartView.as_view(), name='visitor_chart'),
    path('destination', DestinationView.as_view(), name='destination'),
    path('backup-db', BackupDatabaseView.as_view(), name='backup-db'),
]
