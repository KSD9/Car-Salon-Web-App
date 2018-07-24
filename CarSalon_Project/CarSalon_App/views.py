from django.shortcuts import render,redirect
from .templates.CarSalon_App.auth.registerForm import RegisterForm 
from django.contrib.auth.models import User
from .models import CarAstMar,SoldCars,Appointment
from django.shortcuts import get_list_or_404, get_object_or_404


def application_index(request):
    return render(request,'../templates/CarSalon_App/index.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            #user = authenticate(username=username, password=raw_password)
            #login(request, user)

    else:
        form = RegisterForm()
    return render(request, 'CarSalon_App/auth/register.html', {'form': form})       

def view_all_users(request):
   
    users = User.objects.values('first_name','last_name','username','email','is_superuser')

    context = {'users': users}

    return render (request,'CarSalon_App/user/index.html',context)


'''
Car Views 

'''
def view_all_cars(request):
    cars = CarAstMar.objects.all()
    context = {'cars':cars}
    return render (request,'CarSalon_App/car/index.html',context)

def add_car(request):
    if request.method == 'POST':
    
        car = CarAstMar(

         model = request.POST['model'],
         year = request.POST['year'],
         color = request.POST['dropdown_color'],
         price = request.POST['price'],
         quantity = request.POST['quantity'],
         horsePowers = request.POST['horsePowers'],
         engineType = request.POST['dropdown_engineType'],
         topSpeed = request.POST['topSpeed'],
         zeroToHundredAcceleration = request.POST['zeroToHundredAcceleration'],
         description = request.POST['description'],

        )             
                      
        car.save()
        return redirect('/index')
    return render (request,'CarSalon_App/car/create.html')

def details_car(request,id):
    car = CarAstMar.objects.get( id = id)
    context = {'car' : car}
    return render (request,'CarSalon_App/car/details.html',context)

def edit_car(request,id):
    carToEdit = get_object_or_404(CarAstMar,id = id)
    context = {'car':carToEdit}
    if request.method == 'POST':
        carToEdit.model = request.POST['model']
        carToEdit.year = request.POST['year']
        carToEdit.color = request.POST['dropdown_color']
        carToEdit.price = request.POST['price']
        carToEdit.quantity = request.POST['quantity']
        carToEdit.horsePowers = request.POST['horsePowers']
        carToEdit.engineType = request.POST['dropdown_engineType']
        carToEdit.topSpeed = request.POST['topSpeed']
        carToEdit.zeroToHundredAcceleration = request.POST['zeroToHundredAcceleration']
        carToEdit.description = request.POST['description']
        carToEdit.save()
        return redirect('/index')
    return render (request,'CarSalon_App/car/edit.html',context)

def delete_car_confirmation(request,id):
    carToDelete = get_object_or_404(CarAstMar,id = id)
    context = {'car':carToDelete}
    return render (request,'CarSalon_App/car/delete.html',context)


def delete_car(request,id):
    carToDelete = get_object_or_404(CarAstMar,id = id)
    carToDelete.delete()
    return redirect('/index')


def sell_car(request,id):
    if request.method == 'POST':
        car = get_object_or_404(CarAstMar,id = id)

        initialCarQuantity = car.quantity

        soldCar = SoldCars (carId = car, quantity = int(request.POST['quantity']) )

        if initialCarQuantity >= 0 and initialCarQuantity >= soldCar.quantity:

            soldCar.save()
            car.quantity = initialCarQuantity - soldCar.quantity
            car.save()
            return redirect('/car/sold')
    
def view_all_sold_cars(request):
    cars = SoldCars.objects.all()
    context = {'cars':cars}
    return render (request,'CarSalon_App/car/soldCars.html',context)



def create_appointment(request,id):

     if request.method == 'POST':
        car = get_object_or_404(CarAstMar,id = id)
        appointment = Appointment(startDate = request.POST['startDate'],userId = request.user , carId = car )
        appointment.save()
        return redirect('/index')

def  view_all_appointments(request):
    appoinments = Appointment.objects.all()
    context = {'appointments':appoinments}
    return render (request,'CarSalon_App/appointment/index.html',context)