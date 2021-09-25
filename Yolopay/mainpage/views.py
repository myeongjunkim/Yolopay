from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Yolopay

# Create your views here.
def main(request):
    return render(request, 'main.html')

def calendar(request):
    records = Yolopay.objects.all()

    yolo_cnt = Yolopay.objects.filter(yolo_fire="yolo")
    fire_cnt = Yolopay.objects.filter(yolo_fire="fire")
    yolo_rate= round(len(yolo_cnt)/len(records),2)*100
    fire_rate= round(len(fire_cnt)/len(records),2)*100

    happy_cnt = len(Yolopay.objects.filter(emotion="happy"))
    soso_cnt = len(Yolopay.objects.filter(emotion="soso"))
    wow_cnt = len(Yolopay.objects.fillter(emoton="wow"))
    stupid_cnt = len(Yolopay.objects.fillter(emoton="stupid"))
    sad_cnt = len(Yolopay.objects.fillter(emoton="sad"))
    annoyed_cnt = len(Yolopay.objects.fillter(emoton="annoyed"))

    return render(request, 'calendar.html', {'records':records, 'yolo_rate':yolo_rate, 'fire_rate':fire_rate, 'emotion_cnt':[happy_cnt, soso_cnt, wow_cnt, stupid_cnt, sad_cnt, annoyed_cnt]})

def create(request):
    new_record = Yolopay()
    new_record.body = request.POST['record']
    new_record.emotion = request.POST['emotion']
    new_record.yolo_fire = request.POST['type']
    new_record.date = timezone.now()
    new_record.save()
    # {"body":new_record.body,"emotion":new_record.emotion,"yolo_fire":new_record.yolo_fire,"date":new_record.date}
    return redirect('calendar')