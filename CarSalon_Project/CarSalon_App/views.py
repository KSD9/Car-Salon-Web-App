from django.shortcuts import render,redirect
from .registerForm import RegisterForm 
from django.contrib.auth.models import User
from .models import CarAstMar,SoldCars,Appointment,MyUser,SystemLog,RentedCars
from django.shortcuts import get_list_or_404, get_object_or_404
from .services.emailSender import send_appointment_email,send_info_email
from django.contrib.auth.decorators import login_required , user_passes_test
from django.contrib import messages
from django.http import HttpResponse , HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.views.decorators.csrf import csrf_exempt
import datetime

# Custom Decorator To Check If Logged User Has Admin Rights
def logged_user(view_func=None, login_url='/login'):

    actual_decorator = user_passes_test(
        lambda u: u.is_active,
        login_url=login_url,
    )
    if view_func:
        return actual_decorator(view_func)
    return actual_decorator


def superuser_required(view_func=None, login_url='/index'):

    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_superuser,
        login_url=login_url,
    )
    if view_func:
        return actual_decorator(view_func)
    return actual_decorator

def RentManager_required(view_func=None, login_url='/index'):

    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.role == 'RentManager',
        login_url=login_url,
    )
    if view_func:
        return actual_decorator(view_func)
    return actual_decorator   


def sys_log(request,user,action,dateTime,model):
    sysLog = SystemLog(
        userId = user,
        action = action,
        dateTime = dateTime,
        model = model
    

    )
    sysLog.save()

#Application Index
def application_index(request):
    return render(request,'../templates/CarSalon_App/index.html')

# Veiw For User Registration
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES )
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect("/index")
        messages.add_message(request, messages.INFO,form._errors)
    else:
        form = RegisterForm()
    return render(request, 'CarSalon_App/auth/register.html', {'form': form})       

# Admin View To View All Registered Users
@superuser_required
def view_all_users(request):
    users = MyUser.objects.values('first_name','last_name','username','email','is_superuser')
    context = {'users': users}
    return render (request,'CarSalon_App/user/index.html',context)

'''
Car Views 

'''

def view_all_cars(request):
    cars = CarAstMar.objects.all()
    context = {'cars':cars}
    return render (request,'CarSalon_App/car/index.html',context)

@superuser_required
def add_car(request):
    if request.method == 'POST':

        car = CarAstMar(
         model = request.POST['model'],
         year = request.POST['year'],
         color = request.POST['dropdown_color'],
         price = request.POST['carPrice'],
         quantity = request.POST['quantity'],
         horsePowers = request.POST['horsePowers'],
         engineType = request.POST['dropdown_engineType'],
         topSpeed = request.POST['topSpeed'],
         zeroToHundredAcceleration = request.POST['zeroToHundredAcceleration'],
         image = request.POST['image'],
         description = request.POST['description'],
        )             
        car.save()
        sys_log(request,request.user,'create',datetime.datetime.now(),'car')
        return redirect('/car/index')
    return render (request,'CarSalon_App/car/create.html')

def details_car(request,id):
    car = get_object_or_404(CarAstMar,id = id)
    context = {'car' : car}
    return render (request,'CarSalon_App/car/details.html',context)

@superuser_required
def edit_car(request,id):
    carToEdit = get_object_or_404(CarAstMar,id = id)
    context = {'car':carToEdit}
    if request.method == 'POST':
        carToEdit.model = request.POST['model']
        carToEdit.year = request.POST['year']
        carToEdit.color = request.POST['dropdown_color']
        carToEdit.price = request.POST['carPrice']
        carToEdit.quantity = request.POST['quantity']
        carToEdit.horsePowers = request.POST['horsePowers']
        carToEdit.engineType = request.POST['dropdown_engineType']
        carToEdit.topSpeed = request.POST['topSpeed']
        carToEdit.zeroToHundredAcceleration = request.POST['zeroToHundredAcceleration']
        carToEdit.image = request.POST['image']
        carToEdit.description = request.POST['description']
        carToEdit.save()
        return redirect('/car/index')
    return render (request,'CarSalon_App/car/edit.html',context)

#View To Ask The Admin If It's Sure About Car Deletion
@superuser_required
def delete_car_confirmation(request,id):
    carToDelete = get_object_or_404(CarAstMar,id = id)
    context = {'car':carToDelete}
    return render (request,'CarSalon_App/car/delete.html',context)


@superuser_required
def delete_car(request,id):
    carToDelete = get_object_or_404(CarAstMar,id = id)
    carToDelete.delete()
    return redirect('/car/index')



    



@login_required
def create_appointment(request,id):
     if request.method == 'POST':
        adminEmail  = 'rushhourapp9@gmail.com'
        adminPass   = "!e123456789"

        car = get_object_or_404(CarAstMar,id = id)
        appointment = Appointment(startDate = request.POST['startDate'],userId = request.user , carId = car )
        appointment.save()
      
        app = appointment.carId.model
        user = appointment.userId.first_name
        date = str(request.POST['startDate'])
        emailText = 'Hello '+ user + ' ,You have booked a test drive for : '+  date + 'To try Aston Martin: '+ app

        send_appointment_email(adminEmail,adminPass,request.user.email,'New Appointment',emailText)
        return render(request,'CarSalon_App/appointment/appBooked.html')
     else:

        return redirect('/car/index') 
@superuser_required
def  view_all_appointments(request):
    appoinments = Appointment.objects.all()
    context = {'appointments':appoinments}
    return render (request,'CarSalon_App/appointment/index.html',context)

@login_required    
def appointment_booked(request):
    return render(request,'CarSalon_App/appointments/appBooked.html')    

@csrf_exempt
def receive_email_from_user(request):
    send_info_email(request.POST['email'],request.POST['name'],request.POST['body'])
    return redirect('/index')   

def error_404(request):
    return render(request,'CarSalon_App/error_handlers/404.html')    

@logged_user
def back_office_index (request):
     return render(request,'CarSalon_App/back_office/index.html')    
def system_log_index(request):
    logs = SystemLog.objects.all()
    context= {'logs':logs}
    return render(request,'CarSalon_App/back_office/system_log/index.html',context) 
'''
Rent Cars Views
'''
def rent_cars_index(request):
    cars = RentedCars.objects.all()
    context = {'cars':cars}
    return render(request,'CarSalon_App/back_office/rent_car/index.html',context)   

def create_car_for_rent(request):
    cars = CarAstMar.objects.filter(isRented = False , isForRent=True)
    context = {'cars':cars}
    if request.method == 'POST':
        carModel = CarAstMar.objects.get(id = request.POST['carModel'] )
        rentCar = RentedCars(carId=carModel,startDate=request.POST['startDate'],endDate=request.POST['endDate'], employeId = request.user)
        rentCar.save()
        carModel.isRented = True
        carModel.save()
        return redirect('/car/rent/index') 
    else:
        return render(request,'CarSalon_App/back_office/rent_car/create.html',context)   


def edit_car_for_rent(request,id):
    car = get_object_or_404(RentedCars,id = id)
    context = {'car':car}
    if request.method == 'POST':
        car.startDate = request.POST['startDate']
        car.endDate   = request.POST['endDate']
        car.save()
        return redirect('/car/rent/index') 
    else:
        return render(request,'CarSalon_App/back_office/rent_car/edit.html',context)


def delete_rent_car(request,id):
    car = get_object_or_404(RentedCars,id = id)
    if request.method == 'POST':
        carId = car.carId.id
        car.delete()
        carAst = CarAstMar.objects.get(id = carId)
        carAst.isRented = False
        carAst.save()
        return redirect('/car/rent/index') 
    else:
        return render(request,'CarSalon_App/back_office/rent_car/index.html')


'''
Sell Car Views
'''

def sell_car_index(request):
    cars = CarAstMar.objects.filter(isForRent = False)
    context = {'cars':cars}

    return render(request,'CarSalon_App/back_office/sell_car/index.html',context)   

def sell_car_request(request,id):
    car = get_object_or_404(CarAstMar,id = id)
    car.sellingStatus = "Sell Request"
    car.save()
    return redirect('/car/sell/index') 

def index_sell_car_request(request):
    cars = CarAstMar.objects.filter(sellingStatus = "Sell Request")
    context = {'cars':cars}

    return render(request,'CarSalon_App/back_office/sell_car/sell_request.html',context)   

def sell_car(request,id):
   
        try:
            car = get_object_or_404(CarAstMar,id = id)
            initialCarQuantity = car.quantity
            soldCar = SoldCars (carId = car, quantity = 1,date = datetime.datetime.now(),employeId = request.user )

            if initialCarQuantity >= 0 and initialCarQuantity >= soldCar.quantity:
                soldCar.save()
                car.quantity = initialCarQuantity - soldCar.quantity
                car.sellingStatus = "Sold"
                car.save()
                return redirect('/car/sold')
            else:
                messages.add_message(request, messages.INFO, 'Not Enough Amount .')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

        except Exception:
            messages.add_message(request, messages.INFO, 'Please Enter Valid Date .')
            return redirect('car/index') 


@superuser_required    
def view_all_sold_cars(request):
    cars = SoldCars.objects.all()
    context = {'cars':cars}
    return render(request,'CarSalon_App/back_office/sell_car/sold_cars.html',context) 

'''
User's Views
'''            

def users_index(request):
    users = MyUser.objects.all()
    context = {'users':users}
    return render(request,'CarSalon_App/back_office/users/index.html',context)   


def edit_user(request,id):
    user = get_object_or_404(MyUser,id = id)
    context = {'user':user}
    user.email = request.POST['startDate']
    user.username = request.POST['startDate']
    user.role = request.POST['startDate']
    user.picture = request.POST['startDate']
    user.save()
    return render(request,'CarSalon_App/back_office/users/edit.html',context)  