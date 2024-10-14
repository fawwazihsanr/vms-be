from rest_framework import serializers

from vms.visitor.models import Visitor


class VisitorCreationSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    id_card = serializers.CharField(required=True)
    pic = serializers.CharField(required=True)
    vendor = serializers.CharField(required=True)
    check_in_date = serializers.DateTimeField(required=True)
    check_out_date = serializers.DateTimeField(required=False)
    company = serializers.CharField(required=True)
    address = serializers.CharField(required=True)
    mobile_phone = serializers.CharField(required=True)
    dob = serializers.DateField(required=True)
    person_to_visit_name = serializers.CharField(required=True)
    place = serializers.CharField(required=True)
    image = serializers.ImageField(required=True)
