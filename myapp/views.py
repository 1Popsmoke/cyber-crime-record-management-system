from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Complaint
from .forms import ComplaintForm  # Assuming you have a form to handle updates
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import ComplaintSerializer
from django.contrib.auth.models import User
from django.contrib.auth.models import auth
from django.contrib import messages
# Create your views here.
def mainpage(request):
    return render(request, 'mainpage.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        
        if password != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('register') 
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Emaail Already Used.')
            return redirect('register')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Username Already Used.')
            return redirect("register")
        else:
            User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, "Registration successful!")
        
            return redirect('login')  
        
    return render(request, 'register.html') 

    

def login_views(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect ('mainpage')
        else: 
            messages.info (request, 'Credentials Invalid')  
            return redirect('login')
    else:
        return render (request, 'login.html')   


def logout (request):
    auth.logout(request)
    return redirect ('mainpage')      



def team(request):
    return render(request, 'team.html')




def list_complaints(request):
    complaints = Complaint.objects.all()
    return render(request, 'complaints/list_complaints.html', {'complaints': complaints})



@login_required  # Make sure only logged-in users can view
def view_complaint(request, pk):
    """
    View the details of a specific complaint/crime.
    """
    complaint = get_object_or_404(Complaint, pk=pk)
    return render(request, 'complaints/view_complaint.html', {'complaint': complaint})

# View to edit a specific complaint (crime)
@login_required  # Only logged-in users can edit complaints
def update_complaint(request, pk):
    """
    Update a specific complaint/crime report.
    """
    complaint = get_object_or_404(Complaint, pk=pk)

    if request.method == 'POST':
        form = ComplaintForm(request.POST, instance=complaint)
        if form.is_valid():
            form.save()
            return redirect('view_complaint', pk=complaint.pk)  # Redirect to the updated complaint view
    else:
        form = ComplaintForm(instance=complaint)

    return render(request, 'complaints/update_complaint.html', {'form': form})

# API view to get complaint details in JSON (if using API calls)
@api_view(['GET'])
def api_view_complaint(request, pk):
    """
    Get complaint details in JSON format.
    """
    try:
        complaint = Complaint.objects.get(pk=pk)
    except Complaint.DoesNotExist:
        return JsonResponse({'error': 'Complaint not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = ComplaintSerializer(complaint)
    return JsonResponse(serializer.data)

def online_awerness(request):
    return render(request, 'online_awerness.html')

def general_tips(request):
    return render(request, 'general_tips.html')