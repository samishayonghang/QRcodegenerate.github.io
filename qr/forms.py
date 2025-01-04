from django import forms
from.models import QRcode
class QRcodeform(forms.Form):
    fileurl=forms.CharField(max_length=300,
                          required=True,
                          label="File URL",
                          widget=forms.TextInput(attrs={'placeholder':'Enter the URL to generate QRcode!','class':'form-control', 'style': 'width: 20%; height:30px;'})

                           )

class textqrform(forms.Form):
    text=forms.CharField(max_length=300, required=True,label="Text", widget=forms.TextInput(attrs={'placeholder':'Enter your text to generate QRcode','style':'width:20%; height:30px;'}))


class QRDownloadForm(forms.Form):
    pass