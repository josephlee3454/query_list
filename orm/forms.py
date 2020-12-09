from  django.forms import ModelForm
from .models import * 
    
class UserName(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
