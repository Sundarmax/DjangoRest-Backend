from django.shortcuts import render
from .models import Video,Content,Employee,Department
from django.db.models import Sum,Count
import uuid
import datetime

#Model inhertiance establish 1:1 Relationships b/w two models. 
def TestModelInheritance():
    test  =  uuid.uuid4() 
    TDate = datetime.date.today() 
    videoIns = Video()
    videoIns.video_id = test
    #Base class content Table
    videoIns.content_createddate = TDate
    videoIns.content_modifieddate= TDate
    videoIns.content_headline = "Rural Development"
    videoIns.content_title = "Industrial Evolution"
    videoIns.content_slug = "New Revolution"
    videoIns.save()
    print('Record inserted')

#TestModelInheritance()
def TestAggregation():
    # values returns python dict's instead of queryset objects. 
    empIns = list(Employee.objects.values('id','emp_name'))
    print(empIns)
    # Get total no of employees by using inbuild function
    empCount = Employee.objects.all().count()
    # Get count by using aggregate function
    emp_count = Employee.objects.all().aggregate(total = Count('id'))
    total_pay = Employee.objects.all().aggregate(total = Sum('pay'))
    print(emp_count)
    print(total_pay)
    #print(empCount)
    # Get count of Employee by specific department. 
    deptIns = Department.objects.filter(dept_name = "Information Technology").aggregate(total = Count('employee'))
    #print(deptIns)
    # Get count of Employee by each department 
    #dept_Ins = Employee.objects.values('department_dept_name').annotate(Count('id'))
    dept_Ins = Employee.objects.values('department__dept_name').annotate(Count('id'))
    print(dept_Ins)
    MaxDeptEmp=Employee.objects.values('department__dept_name', 'level__level_name').annotate(employee_count = Count('id')).order_by('-employee_count')[:1]
    print(MaxDeptEmp)
    
TestAggregation()

