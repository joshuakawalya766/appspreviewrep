from django.shortcuts import render, redirect
from .models import House
# from .models import  HouseForm

# Create your views here.
def index(request):
    """Search functionality"""
    search_input = request.GET.get('search_fhtml')
    if search_input:
        context={
            'houses': House.objects.filter(title__icontains=search_input),
            'search_input': search_input
        }
    else:
        context = {
            'houses': House.objects.all()
        }
        search_input=''

    """Save info from user on index page """
    if request.method=='POST':
        new_house=House(
            title=request.POST['title_fhtml'],
            location=request.POST['location_fhtml'],
            rooms=request.POST['rooms_fhtml'],
            baths=request.POST['baths_fhtml'],
            image= request.FILES['image_fhtml']
        )
        new_house.save()
        # -----------------using forms
        # form = HouseForm(request.POST, request.FILES)
        # if form.is_valid():
        #     image = request.FILES['image_fhtml']
        #     form.save()
        return redirect('/')
    return render(request, 'house/index.html', context)
    

def base(request):
    context = {
        'houses': House.objects.all()
    }
    return render(request, 'base.html', context)

def houseProfile(request,pk):
    context = {
        'house': House.objects.get(id=pk)
    }
    return render(request, 'house/houseProfile.html', context)
    

def editHouse(request,pk):
    """Save update from use on edit page """
    context = {
        'house': House.objects.get(id=pk)
    }
    
    if request.method=='POST':
        context['house'].title = request.POST['title_fhtml']
        context['house'].location = request.POST['location_fhtml']
        context['house'].rooms = request.POST['rooms_fhtml']
        context['house'].baths = request.POST['baths_fhtml']
        context['house'].image = request.FILES['image_fhtml']
        context['house'].save()
        return redirect('/profile/'+str(context['house'].id))
    
    return render(request, 'house/editHouse.html', context)
    

def deleteHouse(request,pk):
    context = {
        'house': House.objects.get(id=pk)
    }
    if request.method=='POST':
        context['house'].delete()
        return redirect('/')
    return render(request, 'house/deleteHouse.html', context)
    
