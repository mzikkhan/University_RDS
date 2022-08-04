
from django.shortcuts import render
from . import courseadd
# Create your views here.
def homepage(request):
    return render(request,"homepage.html")

def course_add(request):
    if request.method=='POST':
        id=request.POST['courseID']
        name=request.POST['courseName']
        description=request.POST['description']
        
        course=courseadd.CourseAdd(id,name,description)
        course.addCourse()
    return render(request, 'course_add.html')

def course_drop(request):
    
    if request.method=='POST':
        id=request.POST['courseID']
        course=courseadd.CourseAdd(id)
        course.deleteCourse()
    
    return render(request,'course_drop.html')
def course_registration(request):
    return render(request, 'course_registration.html')
def personal_information(request):
    return render(request, 'personal_information.html')
def results(request):
    return render(request, 'results.html')
def student_registration(request):
    return render(request, 'student_registration.html')
