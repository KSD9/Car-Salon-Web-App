from django.shortcuts import render,redirect
from .templates.CarSalon_App.auth.registerForm import RegisterForm 
from django.contrib.auth.models import User
from .models import CarAstMar 


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
    carToEdit = CarAstMar.objects.get (id = id)
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
    carToDelete = CarAstMar.objects.get (id = id)
    context = {'car':carToDelete}
    return render (request,'CarSalon_App/car/delete.html',context)


def delete_car(request,id):
    carToDelete = CarAstMar.objects.get(id = id)
    carToDelete.delete()
    return redirect('/index')