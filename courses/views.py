from django.shortcuts import render
from courses.models import Course

# Create your views here.

def admin_dashboard(request):
    courses = Course.objects.all()
    return render(request, 'courses/admin_dashboard.html', {'courses': courses})
