from django.contrib import admin
from lotto.models import GuessNumbers
#from .models import GuessNumbers 같은 폴더에 있을 때 폴더명(lotto)생략가능
# Register your models here.
admin.site.register(GuessNumbers)
