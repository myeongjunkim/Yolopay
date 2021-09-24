from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Yolopay


# Create your views here.
def mainpage(request):
    return render(request, 'mainpage.html')

def calendar(request):
    records = Yolopay.objects.all()
    return render(request, 'calendar.html', {'records':records})

def create(request):
    new_record = Yolopay()
    new_record.body = request.POST['record']
    new_record.emotion = request.POST['emotion']
    new_record.yolo_fire = request.POST['yolo_fire']
    new_record.date = timezone.now()
    new_record.save()
    return redirect('calendar')