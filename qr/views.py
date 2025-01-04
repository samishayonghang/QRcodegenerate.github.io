from django.shortcuts import render,redirect
from.models import QRcode
from.forms import QRcodeform,textqrform,QRDownloadForm
import qrcode
from io import BytesIO
import base64
from django.http import HttpResponse

# Create your views here.
def qrurl(request):
 download_form = QRDownloadForm()
 qr_code_image=None
 if request.method=="POST":
   form=QRcodeform(request.POST)
   if form.is_valid():
    qr_content= form.cleaned_data['fileurl']
    if qr_content:
                qrimg = qrcode.make(qr_content)
                imagio = BytesIO()
                qrimg.save(imagio, format='PNG')
                imagio.seek(0)
                qr_code_image = base64.b64encode(imagio.read()).decode('utf-8')
                download_url = "/textqr_download/"  # Define a download endpoint
                request.session['qr_file_content'] = base64.b64encode(imagio.getvalue()).decode('utf-8')
      
   
 else:
   form=QRcodeform()
  
 return render(request,"qr/home.html",{'form':form  ,'qr_code_image':qr_code_image ,'download_form':download_form})

  
def textqr(request):
 qrcodeimage=None
 if request.method=="POST":
    form=textqrform(request.POST)
    if form.is_valid():
     qrcontent=form.cleaned_data['text']
     qrimage=qrcode.make(qrcontent)
     imageio=BytesIO()
     qrimage.save(imageio,format="PNG")
     imageio.seek(0)
     qrcodeimage=base64.b64encode(imageio.read()).decode('Utf-8')
     request.session['qr_file_content'] = base64.b64encode(imageio.getvalue()).decode('utf-8')
     
      # Redirect to the
 else:
    form=textqrform()
   
 return render(request,"qr/text.html",{'form':form ,'qrcodeimage':qrcodeimage})




