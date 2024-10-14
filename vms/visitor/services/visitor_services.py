from django.db import transaction
from django.db.models import Q, Count
from django.db.models.functions import ExtractWeekDay
from django.forms import model_to_dict

from vms.visitor.models import Visitor, Destination


def get_all_visitor(search_query=''):
    if search_query:
        return Visitor.objects.filter(
            Q(name__icontains=search_query) |  # Search by name
            Q(id_card__icontains=search_query) |  # Search by id_card
            Q(pic__icontains=search_query)  # Search by pic (or other fields you need)
        )
    return Visitor.objects.all().order_by('-pk')


def get_visitor_by_id(visitor_id):
    return Visitor.objects.get(pk=visitor_id)


def create_visitor(data):
    with transaction.atomic():
        visitor_obj = Visitor.objects.create(**data)
        return visitor_obj.id


def update_visitor(visitor_id, data):
    with transaction.atomic():
        visitor_obj = Visitor.objects.get(pk=visitor_id)
        for key, value in data.items():
            setattr(visitor_obj, key, value)
        visitor_obj.save()
        return visitor_obj


def get_visitor_for_chart():
    visitor_counts = Visitor.objects.annotate(
        day_of_week=ExtractWeekDay('created')
    ).values('day_of_week').annotate(
        count=Count('id')
    ).order_by('day_of_week')

    visitor_total_check_in = Visitor.objects.filter(check_out_date__isnull=True).count()

    # Mapping days to counts
    days_map = {i: 0 for i in range(1, 8)}
    for entry in visitor_counts:
        days_map[entry['day_of_week']] = entry['count']

    # Preparing response in order (Monday=1, ..., Sunday=7)
    days_ordered = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    counts_ordered = [
        days_map.get(day, 0)
        for day in [2, 3, 4, 5, 6, 7, 1]  # Monday to Sunday sequence
    ]

    return {
        'days': days_ordered,
        'counts': counts_ordered,
        'total_visitor': sum(counts_ordered),
        'total_checkin': visitor_total_check_in
    }


def get_destination():
    destinations = Destination.objects.all().values_list('name', flat=True)
    return destinations
