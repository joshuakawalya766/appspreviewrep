from django.shortcuts import render, redirect
from .models import Person, Membership

# Create your views here.


def person(request):
    context = {
        # 'people': Person.objects.all(),
        # 'membership': Membership.objects.all(),
        # 'size_choices': Person.ShirtSize
    }
    """Search functionality"""
    search_input = request.GET.get('search_fhtml')
    if search_input:
        context = {
            'people': Person.objects.filter(fname__icontains=search_input),
            'membership': Membership.objects.all(),
            'size_choices': Person.ShirtSize,
            'search_input': search_input,
            'get_client_ip': Person.get_client_ip(request)
        }
    else:
        context = {
            'people': Person.objects.all(),
            'membership': Membership.objects.all(),
            'size_choices': Person.ShirtSize,
            'get_client_ip': Person.get_client_ip(request)
        }
        search_input = ''

    """Save info from user on people page """
    if request.method == 'POST':
        new_person = Person(
            nin=request.POST['nin_fhtml'],
            fname=request.POST['fname_fhtml'],
            lname=request.POST['lname_fhtml'],
            age=request.POST['age_fhtml'],
            email=request.POST['email_fhtml'],
            afile=request.FILES['afile_fhtml'],
            profile=request.FILES['profile_fhtml'],
            size=request.POST['size_fhtml'],
            height=request.POST['height_fhtml'],
            salary=request.POST['salary_fhtml'],
            etime=request.POST['etime_fhtml'],
            etzone=request.POST['etzone_fhtml'],
            fazno=request.POST['fazno_fhtml'],
            ipadd=request.POST['ipadd_fhtml']
        )
        new_person.save()
        return redirect('personpage')


    return render(request, 'examples/person.html', context)
