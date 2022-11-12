from django.shortcuts import redirect, render
from .models import hotel_info
from django.contrib import messages
from .forms import Hotel_info_Form
from rest_framework import viewsets
from .serializers import Hotel_info_serializer
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics


@login_required(login_url='login')
def home(request):
    hotel=hotel_info.objects.all().count()
    hotel_ktm=hotel_info.objects.filter(hotel_city="Kathmandu").count()
    hotel_lalitpur=hotel_info.objects.filter(hotel_city="Lalitpur").count()
    hotel_bhaktapur=hotel_info.objects.filter(hotel_city="Bhaktapur").count()
    hotel_chitwan=hotel_info.objects.filter(hotel_city="Chitwan").count()
    hotel_nagarkot=hotel_info.objects.filter(hotel_city="Nagarkot").count()
    hotel_pokhara=hotel_info.objects.filter(hotel_city="Pokhara").count()
    hotel_butwal=hotel_info.objects.filter(hotel_city="Butwal").count()
    context={
        'hotel_num':hotel,
        'hotel_ktm_num':hotel_ktm,
        'hotel_lalitpur':hotel_lalitpur,
        'hotel_bhaktapur':hotel_bhaktapur,
        'hotel_chitwan':hotel_chitwan,
        'hotel_nagarkot':hotel_nagarkot,
        'hotel_pokhara':hotel_pokhara,
        'hotel_butwal':hotel_butwal
    }
    return render(request,"index.html",context)


@login_required(login_url='login')
def hotel_display(request):
    hotels=hotel_info.objects.all()
    context={
        "hotels":hotels
    }

    return render(request,"Hotel_list.html",context)
@login_required(login_url='login')
def add_hotel(request):
   

    form=Hotel_info_Form
    if request.method == "POST":
        form =Hotel_info_Form(request.POST)
        if form.is_valid():
            total_room=form.cleaned_data.get('total_rooms')
            total_single_room=form.cleaned_data.get('total_single_room')
            total_double_room=form.cleaned_data.get('total_double_room')
            total_family_room=form.cleaned_data.get('total_family_room')
            total_luxary_room=form.cleaned_data.get('total_luxary_room')
            total_added_room=total_single_room+total_double_room+total_family_room+total_luxary_room
            print('===================================================')
            print(total_room)
            print(total_added_room)
            if total_added_room<= total_room:
                form.save()
                messages.success(request,"Successfully added to the Database and Created API")
                return redirect('hotels_list')
            elif total_added_room>total_room :
                messages.error(request,"Total hotel room did not matched")
                return redirect('add_hotel') 
        else:
            messages.error(request,"Failed to add data in database and API")
    context={
        'form':form
    }
    return render(request,"hotel_admin.html",context) 

@login_required(login_url='login')
def edit_hotel(request,slug):
    hotel=hotel_info.objects.get(slug=slug)
    form= Hotel_info_Form(instance=hotel)
    if request.method == "POST":
        form =Hotel_info_Form(request.POST,instance=hotel)
        if form.is_valid():
            form.save()
            return redirect('hotels_list')
    context={
        'forms':form
    }
    return render(request,"edit_hotel.html",context)
@login_required(login_url='login')
def del_hotel(request,slug):
    hotel=hotel_info.objects.filter(slug=slug)
    hotel.delete()
    messages.success(request,"sucsessfully deleted the Hotel data")
    return redirect('hotels_list')


class hotel_list_api(viewsets.ReadOnlyModelViewSet):
    queryset = hotel_info.objects.all()
    serializer_class = Hotel_info_serializer
    # login_url = 'login'

class Hotel_detail(generics.RetrieveAPIView):
    queryset = hotel_info.objects.all()
    serializer_class = Hotel_info_serializer
    lookup_field="slug"




    
class hotel_place_api(generics.ListAPIView):
    queryset = hotel_info.objects.all()
    serializer_class = Hotel_info_serializer
    # login_url = 'login'
    filter_backends  = (DjangoFilterBackend,)
    filterset_fields  = ('hotel_city',)


def auth_hotel(request):
    form =AuthenticationForm
    
    if request.method == "POST":
        form =AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request,"Admin Logged in successfully!")
                return redirect('home')

            else:
                messages.error(request,"Failed to Logged in!")
    context={
        'form':form
    }

    return render(request,'login.html',context)

def city_hotel(request,slug):
    hotels=hotel_info.objects.filter(hotel_city=slug)
    context={
        "hotels":hotels,
        "slug":slug
    }
    return render(request,"city_detail_hotel.html",context)



















 # if request.method == "POST":
    #     hotel_name=request.POST.get('hotelname')
    #     hotel_address=request.POST.get('hoteladdress')
    #     hotel_city=request.POST.get('hotelcity')
    #     managers_name=request.POST.get('managername')
    #     phone_number=request.POST.get('phnum')
    #     owner_name=request.POST.get('ownername')
    #     owner_number=request.POST.get('ownerphnum')
    #     total_rooms=request.POST.get('room_num')

    #     single_room=False 
    #     double_room=False 
    #     family_room=False 
    #     luxary_room=False 

    #     roomtype=request.POST.getlist('room_type')
    
    #     for room in roomtype:
    #         if room == "single":
    #             single_room=True
    #         elif room == "double":
    #             double_room=True
    #         elif room == "family":
    #             family_room=True
    #         elif room == "luxary":
    #             luxary_room=True

    #     Hotel=hotel_info.objects.create(hotel_name=hotel_name,hotel_address=hotel_address,
    #     hotel_city=hotel_city,
    #     managers_name=managers_name,
    #     phone_number=phone_number,
    #     owner_name=owner_name,
    #     owner_number=owner_number,
    #     total_rooms=total_rooms,
    #     single_room=single_room,
    #     double_room=double_room,
    #     family_room=family_room,
    #     luxary_room=luxary_room
    #     )

    #     Hotel.save()

    #     messages.success(request,"Successfully added to the Database and Created API")
    #     return redirect('home')