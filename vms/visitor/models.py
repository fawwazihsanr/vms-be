from django.db import models
from django.utils import timezone


class ModelWithAutoTimestamp(models.Model):
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField()

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if self._state.adding:
            self.created = timezone.localtime(timezone.now())
        self.modified = timezone.localtime(timezone.now())
        return super().save(*args, **kwargs)

    class Meta:
        abstract = True


class Visitor(ModelWithAutoTimestamp):
    id = models.AutoField(db_column='visitor_id', primary_key=True)
    name = models.CharField(max_length=255)
    id_card = models.IntegerField()
    pic = models.CharField(max_length=255)
    vendor = models.CharField(max_length=255)
    check_in_date = models.DateTimeField()
    check_out_date = models.DateTimeField(null=True, blank=True)
    company = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    mobile_phone = models.CharField(max_length=20)
    email = models.CharField(max_length=100, null=True, blank=True)
    dob = models.DateField()
    person_to_visit_name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    image = models.ImageField(upload_to='visitor_images', null=True, blank=True)
    status = models.BooleanField(default=False)
    notes = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'visitor'


class Destination(ModelWithAutoTimestamp):
    id = models.AutoField(db_column='destination_id', primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'destination'
