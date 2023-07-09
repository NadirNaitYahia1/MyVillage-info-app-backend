from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import Bus,Pharmacies, Users, Admin
from .serializers import BusSerializer,PharmaciesSerializer,AdminSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import redirect





def gettest(request):
    return JsonResponse('Api is working',safe=False)

@api_view(['GET'])
def getBuses(request):
    buses = Bus.objects.all()
    serializer = BusSerializer(buses, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getPharmacies (request):
    pharmacies = Pharmacies.objects.all()
    serializer = PharmaciesSerializer(pharmacies, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def createBus(request):
    data = request.data 
    print('data', data)  
    
    user_id = data.get('user_id') 
    user = Users.objects.get(user_mobile=user_id)
    b = Bus.objects.create(
        # bus_id=(data.get('bus_id')),
        user_id=user,
        bus_name=data.get('bus_name'),
        bus_time=data.get('bus_time'),
        bus_date=data.get('bus_date'),
        bus_from=data.get('bus_from'),
        bus_to=data.get('bus_to'),       
		bus_image=data.get('bus_image')
    )
    print('im here')
    
    serializer = BusSerializer(b, many=False)
    print(serializer.data)
    
    return Response(serializer.data)






@api_view(['POST'])
def createPharmacy(request):
    
    data = request.data
    user_id = data.get('user_id')
    user = Users.objects.get(user_mobile=user_id)
    
    f =  Pharmacies.objects.create(
	    user_id=user,
	    pharmacy_name = data.get('pharmacy_name'),
	    pharmacy_address = data.get('pharmacy_address'),
	    pharmacy_image = data.get('pharmacy_image')
	    )
    
    serializer = PharmaciesSerializer(f, many=False)
    print(serializer.data)
    
    return Response(serializer.data)

# @api_view(['POST'])
# def login(request):
#     print('')
#     print('----------------------login----------------------')
#     data = request.data
#     print('----------------------------data----------------',data)
#     user = Admin.objects.get(admin_name=data.get('name'))
#     serializer = AdminSerializer(user, many=False)
#     # print('----------------------------user----------------', serializer.data['admin_name'])
#     print('----------------------------ser----------------',(serializer.data['admin_password']))
#     # if data.get('name') == user.get('Admin') and data.get('password') == user.admin_password:
#     print('----------------------loged----------------------')
#     return Response('loged')

@api_view(['POST'])
def login(request):
    data = request.data
    try:
        user = Admin.objects.get(admin_name=data.get('name'))
    except Admin.DoesNotExist:
        print('---------------------- admin not exist ----------------------')
        return Response('Invalid credentials', status=400)  

    if data.get('password') == user.admin_password:
        print('----------------------loged----------------------')
        redirect('http://localhost:3000/admin')
        return Response('Logged in successfully', status=200)
    else:
        print('---------------------- mot de passe est faux  ----------------------')
        return Response('Invalid credentials', status=400)
    


@api_view(['PUT'])
def updateBus(request):
    data = request.data
    bus = Bus.objects.get(bus_id=data.get('bus_id'))
    serializer = BusSerializer(bus, data=request.data)
    print(bus, serializer)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
