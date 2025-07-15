from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q,Sum,Max,Min,Count,Avg ,Prefetch
def display_dept(request):
    DPTL=DEPT.objects.all()
    d={'DPTL':DPTL}
    return render(request,'display_dept.html',d)
def display_emp(request):
    EMPTL=EMP.objects.all()
    EMPTL=EMP.objects.filter(deptno=20).order_by(Length('ename').desc())
    EMPTL=EMP.objects.filter(hiredate__day='06') 
    EMPTL=EMP.objects.filter(ename__startswith='M')
    EMPTL=EMP.objects.filter(hiredate__endswith='6')
    EMPTL=EMP.objects.filter(hiredate__startswith='2025')
    EMPTL=EMP.objects.filter(hiredate__contains='1')
    EMPTL=EMP.objects.filter(hiredate__day='6')
    EMPTL=EMP.objects.filter(hiredate__year='2025')
    EMPTL=EMP.objects.filter(hiredate__month='2')
    EMPTL=EMP.objects.filter(hiredate__endswith='6')
    EMPTL=EMP.objects.filter(hiredate__in=('2025-03-6','2025-03-13'))
    EMPTL=EMP.objects.filter(ename__in=('BLAKE','MURALI KRISHNA PATHI'))
    EMPTL=EMP.objects.filter(ename__regex=r'\w')
    EMPTL=EMP.objects.filter(deptno=30,sal__gte=2300)
    EMPTL=EMP.objects.filter(hiredate__gte='2024-01-01')
    EMPTL=EMP.objects.filter(hiredate__lte='2025-03-06')
    EMPTL=EMP.objects.filter(Q(deptno=30)|Q(deptno=20)).order_by(Length('ename').desc())



    d={'EMPTL':EMPTL}
    return render(request,'display_emp.html',d)
def display_salgrade(request):
    SGPTL=SALGRADE.objects.all()
    d={'SGPTL':SGPTL}
    return render(request,'display_salgrade.html',d)

def insert_dept(request):
    deptno=int(input())
    dname=input()
    dloc=input()
    Tdo=DEPT.objects.get_or_create(deptno=deptno,dname=dname,dloc=dloc)
    if Tdo[1]:
        DPTL=DEPT.objects.all()
        d={'DPTL':DPTL}
        return render(request,'display_dept.html',d)
    else:
        return render(request,'display_dept.html',d)
def insert_emp(request):
    eno=int(input("enter the number"))
    en=input("enter the name")
    job=input('enter the job')
    sal=float(input("enter the salary"))
    comm=input("enter the commission")
    hiredate=input('Enter the hiredate')
    if comm:
        comm=float(comm)
    else:
        comm=None
    deptno=int(input('enter the deptno'))
    Do=DEPT.objects.get(deptno=deptno)
    mgr=input("enter the MGR")
    if mgr:
        mo=EMP.objects.get(empid=int(mgr))
    else:
        mo=None
    TEO=EMP.objects.get_or_create(empid=eno,ename=en,job=job,sal=sal,comm=comm,hiredate=hiredate,deptno=Do,mgr=mo)
    if TEO[1]:
        EMPTL=EMP.objects.all()
        d={'EMPTL':EMPTL}
        return render(request,'display_emp.html',d)
    else:
        return HttpResponse(f'{TEO} already present')
def empTODeptJoin(request):
    QLEDO=EMP.objects.all().select_related('deptno').filter(sal__gt=2000)
    QLEDO=EMP.objects.all().select_related('deptno').filter(deptno__deptno=10)
    QLEDO=EMP.objects.all().select_related('deptno').filter(deptno__dname='ACCOUNTING')
    QLEDO=EMP.objects.all().select_related('deptno').filter(deptno__dloc='BANGALORE')
    QLEDO=EMP.objects.all().select_related('deptno').filter(deptno__dloc__in=('BANGALORE','NEW YORK'))
    QLEDO=EMP.objects.all().select_related('deptno').filter(mgr__isnull=True)
    QLEDO=EMP.objects.all().select_related('deptno').filter(mgr__isnull=False,deptno=20,deptno__dloc__in=('DALLAS','NEW YORK'))
    QLEDO=EMP.objects.all().select_related('deptno').filter(deptno__in=(10,20))
    QLEDO=EMP.objects.all().select_related('deptno').filter(mgr__isnull=False,deptno__in=(10,30))
    QLEDO=EMP.objects.all().select_related('deptno').filter(sal__lt=3000,deptno__deptno=20)
    QLEDO=EMP.objects.all().select_related('deptno').filter(sal__gte=2000)
    QLEDO=EMP.objects.all().select_related('deptno').filter(deptno__deptno=10 ,sal__lte=5000)
    QLEDO=EMP.objects.all().select_related('deptno').filter(deptno__dname='SOFTWARE',deptno__dloc='BANGALORE')
    QLEDO=EMP.objects.all().select_related('deptno').filter(deptno__dloc='BANGALORE')
    QLEDO=EMP.objects.all().select_related('deptno').filter(deptno__dloc__in=('BANGALORE','NEW YORK'))
    QLEDO=EMP.objects.all().select_related('deptno').filter(mgr__isnull=True)
    QLEDO=EMP.objects.all().select_related('deptno').filter(mgr__isnull=False,deptno=20,deptno__dloc__in=('DALLAS','NEW YORK'))
    QLEDO=EMP.objects.all().select_related('deptno').filter(deptno__in=(10,20))
    QLEDO=EMP.objects.all().select_related('deptno').filter(mgr__isnull=False,deptno__in=(10,30))
    QLEDO=EMP.objects.all().select_related('deptno').filter(sal__lt=3000,deptno__deptno=20)
    avg_sal=EMP.objects.aggregate(avg_sal=Avg('sal'))
    print(avg_sal)
    max_Sal=



    max_sal=EMP.objects.values('deptno').annotate(max_sal=Max('sal'))
    print(max_sal)


    
    d={"QLEDO":QLEDO}
    return render(request,'empTODeptJoin.html',d)
def empToMgrJoin(request):
     ELMJT=EMP.objects.select_related('mgr').all()
     ELMJT=EMP.objects.select_related('mgr').filter(mgr__isnull=True)
     
     ELMJT=EMP.objects.select_related('mgr').filter(mgr__isnull=False,deptno=20)
     
     ELMJT=EMP.objects.select_related('mgr').filter(mgr__isnull=True,deptno=20,comm__isnull=False)



     d={'ELMJT':ELMJT}
     return render(request,'empToMgrJoin.html',d)
def EmpToDeptAndMgr(request):
    QLEDMO=EMP.objects.all().select_related('deptno','mgr')
    QLEDMO=EMP.objects.select_related('deptno','mgr').filter(ename='BLAKE')
    QLEDMO=EMP.objects.select_related('deptno','mgr').filter(deptno=20)
    QLEDMO=EMP.objects.select_related('deptno','mgr').filter(sal__gte=1999)
    QLEDMO=EMP.objects.select_related('deptno','mgr').filter(mgr__isnull=False)
    QLEDMO=EMP.objects.select_related('deptno','mgr').filter(mgr__isnull=True)
    QLEDMO=EMP.objects.select_related('deptno','mgr').filter(hiredate__month='3')
    QLEDMO=EMP.objects.select_related('deptno','mgr').filter(hiredate__year='2024')
    QLEDMO=EMP.objects.select_related('deptno','mgr').filter(hiredate__year='2025')
    QLEDMO=EMP.objects.select_related('deptno','mgr').filter(hiredate__day='6')
    QLEDMO=EMP.objects.select_related('deptno','mgr').filter(deptno__dloc='BANGALORE')
    QLEDMO=EMP.objects.select_related('deptno','mgr').filter(deptno__deptno='30')
    QLEDMO=EMP.objects.select_related('deptno','mgr').filter(deptno__dname='ACCOUNTING')
    QLEDMO=EMP.objects.select_related('deptno','mgr').filter(deptno__dloc__in=('NEW YORK','BANGALORE'))
    QLEDMO=EMP.objects.select_related('deptno','mgr').filter(deptno__deptno__in=('20','30'))
    QLEDMO=EMP.objects.select_related('deptno','mgr').filter(deptno__dname__in=('ACCOUNTING','SALES')).order_by(Length('ename').desc())
    QLEDMO=EMP.objects.select_related('deptno','mgr').filter(mgr__isnull=True)


    d={'QLEDMO':QLEDMO}
    return render(request,'EmpToDeptAndMgr.html',d)


def empToDeptPr(request):
    
    QLDTO=DEPT.objects.prefetch_related('emp_set').all()
    QLDTO=DEPT.objects.prefetch_related(Prefetch('emp_set',queryset=EMP.objects.filter(ename='BLAKE')))


    d={'QLDTO':QLDTO}
    return render(request,'empToDeptPr.html',d)
