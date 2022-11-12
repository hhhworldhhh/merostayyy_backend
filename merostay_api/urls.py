from django.urls import path,include
from .views import home,add_hotel,hotel_display,edit_hotel,hotel_list_api,del_hotel,auth_hotel,city_hotel,hotel_place_api,Hotel_detail
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('hotel',hotel_list_api,basename="hotel_api")
# router.register('hotel_city',hotel_place_api,basename="hotel_place_api")

urlpatterns=[
    path('',home,name="home"),
    path('add',add_hotel,name="add_hotel"),
    path('hotels',hotel_display,name="hotels_list"),
    path('edit/<str:slug>',edit_hotel,name="edit_hotel"),
    path('delete/<str:slug>',del_hotel,name="del_hotel"),
    path('api/',include(router.urls)),
    path('login/',auth_hotel,name="login"),
    path('hotelcity/<str:slug>',city_hotel,name="hotelcity"),
    path('hotel_city',hotel_place_api.as_view(),name="hotel_city"),
    path('hotel_detail/<str:slug>',Hotel_detail.as_view(),name="hotel_detail"),
]