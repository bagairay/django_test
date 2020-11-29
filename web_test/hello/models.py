from django.db import models

# Create your models here.

class Friend(models.Model):#DB Friend作る　models.Modelでカスタマイズ
    name = models.CharField(max_length=100)#100文字まで
    mail = models.EmailField(max_length=100)
    gender = models.BooleanField()
    age = models.IntegerField(default=0)
    birthday = models.DateField()
    
    def __str__(self):
        return '<Friend:id=' +str(self.id) +','+self.name+'('+str(self.age)+')>'#レコード