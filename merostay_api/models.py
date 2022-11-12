from multiprocessing import managers
from django.utils.text import slugify
from django.db import models

room_type_hotel=(
    ('Single','Single'),
    ('Double','Double'),
    ('Family','Family'),
    ('Luxary','Luxary')
)

city_type=(
    ('Kathmandu','Kathmandu'),
    ('Lalitpur','Lalitpur'),
    ('Bhaktapur','Bhaktapur'),
    ('Chitwan','Chitwan'),
    ('Nagarkot','Nagarkot'),
    ('Pokhara','Pokhara'),
    ('Butwal','Butwal')

)

type_of_property=(
    ('Hotel','Hotel'),
    ('Resort','Resort'),
    ('Hostel/PG','Hostel/PG')
)

class hotel_info(models.Model):
    hotel_name=models.CharField(max_length=100,null=False,blank=False)
    hotel_address=models.CharField(max_length=100,null=False,blank=False)
    hotel_city=models.CharField(max_length=20,choices=city_type,null=True,blank=True)
    property_type=models.CharField(max_length=20,choices=type_of_property,null=False,blank=False)
    managers_name=models.CharField(max_length=100,null=False,blank=False)
    phone_number=models.CharField(max_length=14,null=False,blank=False)
    owner_name=models.CharField(max_length=100,null=True,blank=True)
    owner_number=models.CharField(max_length=100,null=True,blank=True)
    total_rooms=models.IntegerField()
    total_single_room=models.IntegerField(default=0)
    single_room_price=models.CharField(max_length=1000,blank=True,null=True)
    total_double_room=models.IntegerField(default=0)
    double_room_price=models.CharField(max_length=1000,blank=True,null=True)
    total_family_room=models.IntegerField(default=0)
    family_room_price=models.CharField(max_length=1000,blank=True,null=True)
    total_luxary_room=models.IntegerField(default=0)
    luxary_room_price=models.CharField(max_length=1000,blank=True,null=True)
    tv_room=models.BooleanField('tv_room',default=False)
    balcony_room=models.BooleanField('balcony_room',default=False)
    coffe_maker_service=models.BooleanField('coffe_maker',default=False)
    laundary_service=models.BooleanField('laundary_service',default=False)
    smoking_room=models.BooleanField('smoking_room',default=False)
    full_time_service=models.BooleanField('24/7_service',default=False)
    resturant=models.BooleanField('resturant',default=False)
    slug=models.SlugField(blank=True)
    

    def __str__(self):
        return self.hotel_name

    def save(self, *args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.hotel_name)
        super().save(*args,**kwargs)

