from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    #student
    path('students/', views.student_list, name='student_list'),
    path('students/add/', views.student_create, name='student_create'),
    path('students/<int:student_id>/', views.student_detail, name='student_detail'),
    path('students/<int:student_id>/edit/', views.student_edit, name='student_edit'),
    path('students/<int:student_id>/delete/', views.student_delete, name='student_delete'),

    #teacher
    path('teachers/',views.teacher_list, name= 'teacher_list'),
    path('teachers/add/',views.teacher_create, name= 'teacher_create'),
    path('teachers/<int:teacher_id>/edit/',views.teacher_edit, name='teacher_edit'),
    path('teachers/<int:teacher_id>/delete/',views.teacher_delete, name='teacher_delete'),

    #classes

    path('classes/', views.class_list, name='class_list'),
    path('classes/add/', views.class_create, name='class_create'),
    path('classes/<int:class_id>/edit/', views.class_edit, name='class_edit'),
    path('classes/<int:class_id>/delete/', views.class_delete, name='class_delete'),

    #parents
    path('parents/', views.parent_list, name='parent_list'),
    path('parents/add/', views.parent_create, name='parent_create'),
    path('parents/<int:parent_id>/edit/', views.parent_edit, name='parent_edit'),
    path('parents/<int:parent_id>/delete/', views.parent_delete, name='parent_delete'),

    #notification
    path('notifications/', views.notification_list, name='notification_list'),
    path('notifications/send/', views.notification_create, name='notification_create'),
    #======= notif
    path('attendance/<int:student_id>/record/',views.record_attendance,name='record_attendance'),

    #fee
    path('fees/', views.fee_list, name='fee_list'),
    path('fees/create/', views.fee_create, name='fee_create'),
    path('fees/<int:fee_id>/pay/', views.record_payment, name='record_payment'),
    
    #student==Enroll
    path('students/enroll/',views.student_enroll,name='student_enroll'),
    #parent Quick
    path('parents/quick-add/',views.quick_parent_create,name='quick_parent_create'),
]




