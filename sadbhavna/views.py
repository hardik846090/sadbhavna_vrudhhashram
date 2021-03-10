from django.shortcuts import render, redirect

from .models import Benner, WhatWeDo, Volunteer, Cause, LatestNews, UpcomingEvents, Contact


# Create your views here.

def index(request):
    bennerList = Benner.objects.all()
    whatwedoList = WhatWeDo.objects.order_by('-id')
    volunteerList = Volunteer.objects.all()
    causeList = Cause.objects.all()
    latestNewsList = LatestNews.objects.all()
    upcomingEventList = UpcomingEvents.objects.all()
    date = UpcomingEvents.objects.all().values('date')
    for i in date.values():
        idate = i['date']
        print(idate)
    return render(request, 'index.html',
                  {'bennerList': bennerList, 'whatwedoList': whatwedoList, 'volunteerList': volunteerList,
                   'causeList': causeList, 'latestNewsList': latestNewsList, 'upcomingEventList': upcomingEventList,
                   'idate': idate})


def index2(request):
    return render(request, 'index-2.html')


def index3(request):
    return render(request, 'index-3.html')


def about(request):
    whatwedoList = WhatWeDo.objects.order_by('-id')
    causeList = Cause.objects.all()
    volunteerList = Volunteer.objects.all()
    return render(request, 'about.html',
                  {'whatwedoList': whatwedoList, 'causeList': causeList, 'volunteerList': volunteerList})


def cause(request):
    causeList = Cause.objects.all()
    return render(request, 'causes.html', {'causeList': causeList})


def cause_single(request):
    return render(request, 'causes-single.html')


def event(request):
    upcomingEventList = UpcomingEvents.objects.all()
    return render(request, 'event.html', {'upcomingEventList': upcomingEventList})


def event_single(request):
    return render(request, 'event-single.html')


def donate(request):
    return render(request, 'donate.html')


def volunteer(request):
    volunteerList = Volunteer.objects.all()
    return render(request, 'volunteer.html', {'volunteerList': volunteerList})


def error(request):
    return render(request, 'error.html')


def blog(request):
    upcomingEventList = UpcomingEvents.objects.all()
    print("????????????????????????????????????????", upcomingEventList)
    return render(request, 'blog.html', {'upcomingEventList': upcomingEventList})


def blog_left(request):
    return render(request, 'blog-left.html')


def blog_fulwidth(request, foo):
    upcomingEventList = UpcomingEvents.objects.get(pk=foo)
    print("????????????????????????????????????????", upcomingEventList.id)
    return render(request, 'blog-fulwidth.html', {'title': upcomingEventList.title, 'image': upcomingEventList.image,
                                                  'description': upcomingEventList.description,
                                                  'date': upcomingEventList.date})


def blog_single(request):
    return render(request, 'blog-single.html')


def blog_single_left(request):
    return render(request, 'blog-single-left.html')


def blog_single_fluid(request):
    return render(request, 'blog-single-fluid.html')


def contact(request):
    thank = False
    if request.method == "POST":
        fname = request.POST.get("fname", "")
        lname = request.POST.get("lname", "")
        email = request.POST.get("email", "")
        subject = request.POST.get("subject", "")
        desc = request.POST.get("desc", "")
        contact = Contact(fname=fname, lname=lname, email=email, subject=subject, desc=desc)
        contact.save()
        thank = True
    return render(request, 'contact.html', {'thank': thank})
