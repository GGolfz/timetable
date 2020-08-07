from django.http import HttpResponse,HttpResponseBadRequest
from . import models
import json
import random
from django.views.decorators.csrf import csrf_exempt

def getTime(time):
    t = time.split('.')
    h = int(t[0])
    m = int(t[1])
    return h*60+m
def check(day,start,end):
    check = True
    for i in models.Subject.objects.values('starttime','endtime').filter(day=day).all():
        time_start = i['starttime']
        time_end = i['endtime']
        if not ((getTime(start) <= getTime(time_start) and getTime(end) <= getTime(time_start)) or (getTime(start) >= getTime(time_end) and getTime(end)>= getTime(time_end))):            
            check = False
    return check
def getSubject():
    response = list()
    for subject in models.Subject.objects.all():
        response.append({
            "subject_code": subject.subject_code,
            "subject_name": subject.subject_name,
            "lecturer": subject.lecturer,
            "room": subject.room,
            "day": subject.day,
            "starttime": subject.starttime,
            "endtime": subject.endtime,
            "color": subject.color
        })
    return response
def getColor(subject):
    colors = ["#C7A8DA","#FFA3A5","#FDE3A6","#B2D570","#4CDDB4","#73E8F2","#42A5F5","#97CFDE","#F8B195","#FDD998","#FFACB7","#DBC6EB","#EFBBCF","#FFD5CD"]
    for i in models.Subject.objects.values('color').all():
        if i['color'] in colors:
            colors.remove(i['color'])
    sub = models.Subject.objects.filter(subject_code=subject).all()
    if len(sub) > 0 :
        return sub[0].color
    else:
        print(colors)
        return colors[random.randint(0,len(colors)-1)]
@csrf_exempt 
def subject(request):
    if request.method == 'GET':
        response = getSubject()
        return HttpResponse(json.dumps(response),content_type='application/json')
    elif request.method == 'POST':
        data = request.body.decode("utf-8") 
        subject = json.loads(data)
        color = getColor(subject["subject_code"])
        if check(subject["day"],subject["starttime"],subject["endtime"]) :
            models.Subject.objects.create(subject_code=subject["subject_code"],
                                        subject_name=subject["subject_name"],
                                        lecturer=subject["lecturer"],
                                        room=subject["room"],
                                        day=subject["day"],
                                        starttime=subject["starttime"],
                                        endtime=subject["endtime"],
                                        color=color)
            response = getSubject()
            return HttpResponse(json.dumps(response),content_type='application/json')
        else:
            return HttpResponseBadRequest()
@csrf_exempt 
def clear(request):
    if request.method == 'POST':
        models.Subject.objects.all().delete()
        response = getSubject()
        return HttpResponse(json.dumps(response),content_type='application/json')