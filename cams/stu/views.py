from django.shortcuts import render,redirect, HttpResponseRedirect,HttpResponse
# from .forms import SignUpForm, EditUserProfileForm, EditAdminProfileForm, registration_form
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth import authenticate, login, logout,hashers
from django.contrib.auth.models import User, Group,auth
from stu.models import Student,Student_status,Contact
from datetime import datetime, timedelta

# Create your views here.
def home(request):
  
  return render(request,'stu/index.html')

  
# Signup View Function
def signup(request):
  if request.method =='POST':

    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username = request.POST['username']
    email = request.POST['email']
    password1 = request.POST['password1']
    password2 = request.POST['password2']
    if password1== password2:
      if User.objects.filter(username=username).exists():
        messages.info(request,'user name exist')
        
        return redirect('/signup/')
      elif User.objects.filter(email=email).exists():
        messages.info(request,'email  taken try another email')
        
        return redirect('/signup/')
      else:

        user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password = password1)
        
        user.save()
        
        messages.info(request,'Account Successfully created')
        
        return redirect('/login/')
    else:
      messages.info(request,"password do't match")
      
      return redirect('/signup/')
  else:  
    return render(request,'stu/signup.html')
    
    



  
  

# Login View Function
def login(request):

  if request.method=='POST':
    username=request.POST['username']
    password1=request.POST['password1']
    user = auth.authenticate(username=username ,password=password1)

    if user is not None:
      auth.login(request,user)
      return redirect("/profile/")
    else:
      messages.info(request,'Username and Password not Match')
      return render(request, 'stu/login.html')
  else:

    return render(request, 'stu/login.html')
  


def user_logout(request):
    logout(request)
    # Redirect to a success page.
    messages.success(request,'Logout Succesfully')
    return redirect('/login/')

    
  




def profile(request):
  if request.user.is_authenticated:
    return render(request,'stu/profile.html',{'name':request.user})
  else:

    return redirect('/login/')

def admission_form(request):
  
    
  
  if request.method=='POST':
      
    c_name = request.POST['course_name']
        
    S_name = request.POST['s_name']
    F_name = request.POST['f_name']
    M_name = request.POST['m_name']
    Gender = request.POST['gender']
          
    Category = request.POST['category']
    Dob = request.POST['dob']
    Mo_no= request.POST['mo_no']
    Email = request.POST['email']
          
    Village = request.POST['village']
    Distic = request.POST['distic']
    State = request.POST['state']
    Pin_code = request.POST['pin_code']

    Board_name = request.POST['board_name']
    Ten_marks = request.POST['ten_marks']
    Tw_board= request.POST['tw_board']
    Tw_marks = request.POST['tw_marks']
    University = request.POST['university']
    Graduation = request.POST['graduation']

    
  
        
        
    data =Student(coursename=c_name,studentname=S_name,fathername=F_name,mothername=M_name,emall=Email,gender=Gender,category=Category,dob=Dob,mono=Mo_no,village=Village,distic=Distic,state=State,pincode=Pin_code,boardname=Board_name,tenmarks=Ten_marks,twboard=Tw_board,twmarks=Tw_marks,university=University,graduation=Graduation)
    
    data.save()
    messages.success(request,'you aplication successfully submited') 
    
   
    response=redirect('/profile/')
    response.set_cookie('name', S_name, expires=datetime.utcnow()+timedelta(days=100))
   
    

    return response
 
 
    

          
  else:

    names = request.COOKIES.get('name')
    
    return render(request,'stu/registration.html',{'name':request.user,'nm':names })
   

def contact(request):
  pass 
 
   
    
    

    
   
   

  
    
    

    
      

      
   
    
    
    

    

    
      

    
  
   
    
   
    
    
    
