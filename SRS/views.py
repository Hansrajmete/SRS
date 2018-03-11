from .shaencrypt import encrypt_string
from django.shortcuts import render
from .image import upload,replace


def index(request):
    import datetime,time
    now = datetime.datetime.now()
    format_iso_now = now.isoformat()
    unixtime = time.mktime(now.timetuple())
    c=int(unixtime)
    en = encrypt_string(str(c))
    print(int(unixtime))
    action=1
    if(action==1):
        upload("Amruta", 3,"/home/super--user/cap.png")
    else:
        replace("Amruta", 2,"/home/super--user/test.png")
    return render(
        request,
        'index.html',
        {'hashkey': en, 'time': c}
    )


