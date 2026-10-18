from django.contrib import admin
# Register your models here.
from.models import (
    AcademicYears , Students, Teachers, Classes,
    Subjects, Enrollments, Attendance, Users,Fees,FeesPayments )

#Adminثبت مدل ها اصلی برای نمایش در پنل 
@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
        list_display = ('student_number','first_name','last_name','status','admission_date',)
        search_fields = ('first_name','last_name','student_number')

@admin.register(Teachers)
class TeacherAdmin(admin.ModelAdmin):
        list_display = ('employee_number','first_name','last_name','status')
        search_fields = ('first_name','last_name','employee_number')
@admin.register(Classes)
class ClassAdmin(admin.ModelAdmin):
        list_display = ('class_name','grade_level')

@admin.register(Fees)
class FeesAdmin(admin.ModelAdmin):
        list_display = ('enrollment','amount','feetype','fee_month','status','due_date')
        list_filter = ('status','feetype','fee_month')
        search_fields  = ('enrollment__student__first_name','enrollment__student__last_name')

@admin.register(FeesPayments)
class FeesPymentsAdmin(admin.ModelAdmin):
        list_display = ('fee','amount','payment_date','receipt_number', 'payment_method')
        search_fields = ('receipt_number','reference_number')
          



admin.site.register(AcademicYears)
admin.site.register(Subjects)
admin.site.register(Enrollments)
admin.site.register(Attendance)
admin.site.register(Users)


