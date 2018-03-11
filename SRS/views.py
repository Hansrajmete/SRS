from .shaencrypt import encrypt_string
from django.shortcuts import render
from django.http import HttpResponseRedirect
#from .image import upload,replace
from .image import sign_up


def index(request):
    import datetime,time
    now = datetime.datetime.now()
    format_iso_now = now.isoformat()
    unixtime = time.mktime(now.timetuple())
    c=int(unixtime)
    en = encrypt_string(str(c))
    print(int(unixtime))
    if request.method == 'POST':# and request.POST.get("Submit_SignUp"):
        username=request.POST.get("Email")
        password=request.POST.get("Password")
        mobile_no=request.POST.get("Mobile")
        print(username)
        print(password)
        print(mobile_no)
        sign_up(username,password,mobile_no)
        return HttpResponseRedirect('/')
    print("HEloo")
    #myForm = CustomForm(request.POST)
    '''action=1
if(action==1):
    upload("Amruta", 3,"/home/super--user/cap.png")
else:
    replace("Amruta", 2,"/home/super--user/test.png")'''
    return HttpResponseRedirect("index")


def myview_job(request):
    return render(
        request,
        'JobOpening.html',
    )
def myview_status(request):
    return render(
        request,
        'Status.html',
    )

def myview_index(request):
    return render(
        request,
        'index.html',
    )