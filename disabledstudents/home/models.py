from django.db import models
from accounts.models import CustUser,Category
# Create your models here.

class Notes(models.Model):
    file=models.FileField(upload_to='media/notes')
    dt=models.DateTimeField(auto_now_add=True,null=True)
    cat=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    # user=models.ForeignKey(CustUser,on_delete=models.CASCADE,related_name='notes');;;;