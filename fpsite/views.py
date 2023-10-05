from django.shortcuts import render
from . import models
from . import forms
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session
from django.db.models import Sum

# Create your views here.
def index(request):
    room = models.Room.objects.all()
    photos = models.Photo.objects.all()
    empty=[]
    for num in room:
        try:
            resident=models.Resident.objects.get(roomnumber = num)
            empty.append("已租")
        except:
            empty.append("空房")
    room_info = zip(room,empty)

    return render(request,'index.html',locals())

def roomdetail(request,r="0"):
    try:
        room = models.Room.objects.get(roomnumber = r)
        photos = models.Photo.objects.filter(roomnumber = room)
    except:
        return HttpResponseRedirect("/")
    return render(request,'roomdetail.html',locals())

# def userinfo(request):
#     return render(request,'userinfo.html',locals())

@login_required(login_url='login/')
def userinfo(request):
    try:
        if request.session['identity'] != 0:
            return HttpResponseRedirect('/')
    except:
        return HttpResponseRedirect('/')
    username = request.user.username
    user = auth.models.User.objects.get(username = username)
    try:
        resident_profile = models.Resident.objects.get(name = user)
        profile = resident_profile


    except:
        profile = models.Resident(name = user)
    if request.method == "POST":
        profile_form = forms.ProfileForm(request.POST, instance = profile )
        if profile_form.is_valid():
            profile_form.save()
            messages.add_message(request, messages.INFO, "個人資料已儲存")
            return HttpResponseRedirect('/')
    else:
        profile_form = forms.ProfileForm()
    return render(request,'userinfo.html',locals())

def login(request):
	if request.method == "POST":
		login_form = forms.LoginForm(request.POST)
		if login_form.is_valid():
			user_name =request.POST["user_name"].strip()
			password = request.POST["password"]
			user = authenticate(username = user_name,password = password)
			if user is not None:
			    if user.is_active:
			        auth.login(request,user)
			        try :
			            account = models.Account.objects.get(name = user)
			        except:
			            account = models.Account.objects.create(name = user,identity = 'non-resident' )
			            account.save()
			        account = models.Account.objects.get(name = user)
			        if account.identity == "resident":
			            request.session['identity'] = 0
			         #   identity = request.session['identity']
			            try:
			                resident = models.Resident.objects.get(name = user)
			                messages.add_message(request,messages.SUCCESS,'login succeed')
			                return HttpResponseRedirect("/")
			            except:
			                messages.add_message(request,messages.INFO,'請先完成用戶資料')
			                return HttpResponseRedirect("/userinfo/")
			        elif account.identity == 'landlord':
			            request.session['identity'] = 1
			         #   identity = request.session['identity']
			            messages.add_message(request,messages.SUCCESS,'房東登入成功')
			            return HttpResponseRedirect("/")
			        elif account.identity == 'non-resident':
			            request.session['identity'] = 2
			         #   identity = request.session['identity']
			            messages.add_message(request,messages.INFO,'等待房東確認為住戶後才可開啟住戶功能!')
			            return HttpResponseRedirect("/")
			    else:
			        messages.add_message(request,messages.WARNING,'Incorrect Password')
			else:
			    messages.add_message(request,messages.WARNING,'User does not exist')
		else:
		    messages.add_message(request,messages.INFO,"檢查輸入欄位")
	else:
	    login_form=forms.LoginForm()
	return render(request,"login.html",locals())
@login_required(login_url='login/')
def booking(request):
    try:
        if request.session['identity'] != 2:
            return HttpResponseRedirect('/')
    except:
        return HttpResponseRedirect('/')
    if request.method =="POST":
        book_form = forms.BookForm(request.POST)
        if book_form.is_valid():
            messages.add_message(request,messages.SUCCESS, "已登記")
            book_form.save()
            return HttpResponseRedirect("/")
        else:
             messages.add_message(request,messages.WARNING, "登記失敗 請檢查欄位")
    else:
        book_form = forms.BookForm()
        messages.add_message(request,messages.INFO, "請填寫完整")
    return render(request,"book.html",locals())

def logout(request):
    auth.logout(request)
    if 'identity' in request.session:
        Session.object.all().delete()
    messages.add_message(request,messages.INFO, "登出成功")
    return HttpResponseRedirect("/")
@login_required(login_url='login/')
def addphoto(request):
    try:
        if request.session['identity'] != 1:
            return HttpResponseRedirect('/')
    except:
        return HttpResponseRedirect('/')
    roomnumber = models.Room.objects.all()
    photos = models.Photo.objects.all()
    if request.method == 'POST':
        form = forms.PhotoForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.INFO, "上傳成功")
    else:
        form = forms.PhotoForm()
        return render(request, 'addphoto.html', locals())
    return render(request, 'addphoto.html', locals())
@login_required(login_url='login/')
def seeuser(request, pid=None):
    if pid:
        try:
            del_resident = models.Resident.objects.get(id=pid)
            del_resident = auth.models.User.objects.get(username = del_resident)
            del_resident.delete()
        except:
            del_resident = None
    try:
        if request.session['identity'] != 1:
            return HttpResponseRedirect('/')
    except:
        return HttpResponseRedirect('/')
    resident = models.Resident.objects.filter(enable=True).order_by("roomnumber")
    roomnumber = models.Room.objects.get(roomnumber="公共區域")

    return render(request, 'seeuser.html',locals())

@login_required(login_url='login/')
def check_book(request):
    try:
        if request.session['identity'] != 1:
            return HttpResponseRedirect('/')
    except:
        return HttpResponseRedirect('/')
    books= models.Book.objects.all()

    return render(request,"check_book.html",locals())

@login_required(login_url='login/')
def electric(request):
    try:
        if request.session['identity'] != 1:
            return HttpResponseRedirect('/')
    except:
        return HttpResponseRedirect('/')
    try:
        startdate = request.POST['startdate']
        enddate = request.POST['enddate']
        totaluse = int(request.POST['totaluse'])
        totalbill = int(request.POST['totalbill'])
        r301 = float(request.POST['r301'])
        r302 = float(request.POST['r302'])
        r303 = float(request.POST['r303'])
        r305 = float(request.POST['r305'])
        ruse = [r301,r302,r303,r305]
    except:
        messages.add_message(request,messages.WARNING, "每個欄位都要填才能計算")
        totalbill = None

    if totalbill != None:
        per_price=totalbill/totaluse
        per_price =round( per_price ,1)
        models.Electricity_total.objects.filter(current="current").update(startdate=startdate,enddate=enddate,
        totaluse=totaluse,totalbill=totalbill,per_price=per_price)
        Etotal=models.Electricity_total.objects.get(current="current")
        r1 = models.Room.objects.get(roomnumber="301")
        r2 = models.Room.objects.get(roomnumber="302")
        r3 = models.Room.objects.get(roomnumber="303")
        r5 = models.Room.objects.get(roomnumber="305")
        room=[r1,r2,r3,r5]

        for i in range(0,4):
            p=models.Electricity_personal.objects.get(roomnumber = room[i])
            pc=float(p.current_use)
            puse = ruse[i]-pc
            puse =round( puse ,1)
            models.Electricity_personal.objects.filter(roomnumber = room[i]).update(last_use=pc,
            current_use=ruse[i],personaluse=puse,pay=False)
        try:
            totalpuse = models.Electricity_personal.objects.all().aggregate(Sum('personaluse'))['personaluse__sum'] or 0.0
            totalpuse=float(totalpuse)
            avgtotaluse = float((totaluse-totalpuse)/4)
            avgtotaluse = round(avgtotaluse,1)

            for i in range(0,4):
                p=models.Electricity_personal.objects.get(roomnumber = room[i])
                puse = float(p.personaluse)
                puse =round( puse ,1)
                bill = (avgtotaluse+puse)*per_price
                bill = round( bill ,0)
                models.Electricity_personal.objects.filter(roomnumber = room[i]).update(avg_totaluse=avgtotaluse,
                bill=bill)
            messages.add_message(request,messages.WARNING, "已公布電費")

        except:
            messages.add_message(request,messages.WARNING,"bad" )
    return render(request,"electric.html",locals())


@login_required(login_url='login/')
def adminelectric(request,rnum=None):
    try:
        if request.session['identity'] != 1:
            return HttpResponseRedirect('/')
    except:
        return HttpResponseRedirect('/')
    if rnum:
        try:
            room = models.Room.objects.get(roomnumber=rnum)
            models.Electricity_personal.objects.filter(roomnumber = room).update(pay = True)
        except:
            room = None
    electotal = models.Electricity_total.objects.get(current="current")
    electperson=models.Electricity_personal.objects.all()
    return render(request, 'admineletric.html',locals())




@login_required(login_url='login/')
def electinfo(request):
    try:
        if request.session['identity'] != 0:
            return HttpResponseRedirect('/')
    except:
        return HttpResponseRedirect('/')
    try:
        resident = models.Resident.objects.get(name = request.user)
        room = models.Room.objects.get(roomnumber = resident.roomnumber.roomnumber)
        electperson = models.Electricity_personal.objects.get(roomnumber = room)
        electotal = models.Electricity_total.objects.get(current="current")
    except:
        messages.add_message(request,messages.WARNING, "查無資料")
        return HttpResponseRedirect('/')

    return render(request,'electinfo.html',locals())
