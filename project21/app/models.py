from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class DEPT(models.Model):
    deptno=models.IntegerField(primary_key=True)
    dname=models.CharField(max_length=100)
    dloc=models.CharField(max_length=100)
    def __str__(self):
        return str(self.deptno)


class EMP(models.Model):
    empid=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=100)
    job=models.CharField(max_length=100)
    sal=models.DecimalField(max_digits=10,decimal_places=2)
    comm=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    hiredate=models.DateField(auto_now=True)
    deptno=models.ForeignKey(DEPT,on_delete=models.CASCADE)
    mgr=models.ForeignKey("self",on_delete=models.SET_NULL,null=True,blank=True)
    def __str__(self):
        return self.ename


class SALGRADE(models.Model):
    grade=models.IntegerField(primary_key=True)
    losal=models.DecimalField(max_digits=10,decimal_places=2)
    hisal=models.DecimalField(max_digits=10,decimal_places=2)
    def __str__(self):
        return str(self.grade)