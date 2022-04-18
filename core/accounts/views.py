from django.http import HttpResponse
from django.shortcuts import render
import PIL.Image as Image
import io
import base64
# Create your views here.
def home(request):
    if request.method=='POST':
        data = request.POST['imageurl']
        newData = data.split(',')[1]
        b=base64.b64decode(newData)
        print('b',b)
        img = Image.open(io.BytesIO(b))
        print(img)
        img.show()
        img.save('My Castle.png')
        return HttpResponse(newData)
    else:
        return render(request,'index.html')