"""
URL configuration for project21 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('insert_emp/',insert_emp,name='insert_emp'),
    path('insert_dept/',insert_dept,name='insert_dept'),
    path('display_dept/',display_dept,name='display_dept'),
    path('display_emp/',display_emp,name='display_emp'),
    path('display_salgrade/',display_salgrade,name='display_salgrade'),
    path('empTODeptJoin/',empTODeptJoin,name='empTODeptJoin'),
    path('empToMgrJoin/',empToMgrJoin,name='empToMgrJoin'),
    path('EmpToDeptAndMgr/',EmpToDeptAndMgr,name='EmpToDeptAndMgr'),
    path('empToDeptPr/',empToDeptPr,name='empToDeptPr'),
]
