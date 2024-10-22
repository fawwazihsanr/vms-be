from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.forms.models import model_to_dict

from vms.standardized_api_response.utils import created_response, success_response, general_error_response
from vms.visitor.serializers import VisitorCreationSerializer
from vms.visitor.services.visitor_services import create_visitor, get_visitor_by_id, \
    get_all_visitor, update_visitor, get_visitor_for_chart, get_destination


class VisitorView(APIView):
    permission_class = [IsAuthenticated]

    def post(self, request):
        visitor_data = request.data
        user = request.user
        serializer = VisitorCreationSerializer(data=visitor_data)
        if serializer.is_valid():
            visitor_data = serializer.validated_data
            visitor_data['created_by'] = user
            create_visitor(visitor_data)
            return created_response({"message": "Visitor created"})
        return general_error_response(serializer.errors)

    def get(self, request, visitor_id=None):
        paginator = PageNumberPagination()
        paginator.page_size = 10
        if visitor_id:
            data = get_visitor_by_id(visitor_id)
            if data:
                data = model_to_dict(data)
                data['image'] = data['image'].url
            return success_response(data)
        search_query = request.GET.get('q', '')
        data = get_all_visitor(search_query)
        result_page = paginator.paginate_queryset(data, request)
        serialized_data = []

        for visitor_obj in result_page:
            visitor = model_to_dict(visitor_obj)

            if visitor_obj.created_by:
                visitor['created_by'] = visitor_obj.created_by.username
            else:
                visitor['created_by'] = "Unknown"

            if visitor_obj.image:
                visitor['image'] = visitor_obj.image.url
            else:
                visitor['image'] = None
            serialized_data.append(visitor)

        total_pages = paginator.page.paginator.num_pages
        return paginator.get_paginated_response({
            'results': serialized_data,
            'total_pages': total_pages
        })

    def put(self, request, visitor_id):
        data = request.data
        visitor = update_visitor(visitor_id, data)
        if visitor:
            visitor = model_to_dict(visitor)
            visitor['image'] = visitor['image'].url
        return success_response(visitor)


class VisitorChartView(APIView):
    permission_class = [IsAuthenticated]

    def get(self, request):
        return success_response(get_visitor_for_chart())


class DestinationView(APIView):
    permission_class = [IsAuthenticated]

    def get(self, request):
        return success_response(get_destination())


import os
import subprocess
from datetime import datetime
from django.http import JsonResponse
from django.views import View
from django.conf import settings

class BackupDatabaseView(View):
    def get(self, request):
        # Define the backup directory and filename
        backup_dir = os.path.join(settings.BASE_DIR, 'backups')
        os.makedirs(backup_dir, exist_ok=True)
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_file = os.path.join(backup_dir, f'database_backup_{timestamp}.json')

        # Run the dumpdata command
        try:
            with open(backup_file, 'w') as f:
                subprocess.call(['python', '-Xutf8', 'manage.py', 'dumpdata'], stdout=f)
            return JsonResponse({'status': 'success', 'message': f'Backup created at {backup_file}'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
