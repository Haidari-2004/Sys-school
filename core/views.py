from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib import messages
from django.db.models import Q
from .models import Students,Classes,Parents, StudentParents
from .models import Teachers,Notifications,NotificationRecipients
from .forms import StudentForm,TeacherForm,ClassForm,Notification_form
from .forms import ParentForm, StudentParentForm,FeeForm, PaymentForm,Enrollments,EnrollmentForm
from .models import Fees, FeesPayments,Users
from django.http import JsonResponse


# Create your views here.

#dashboard
def dashboard(request):
    total_students = Students.objects.count()
    context = {
            'total_students':total_students,
            'total_teachers':28,
            'total_classes': 32,
            'attendance_rate ':'94%',}
    return render(request, 'core/dashboard.html',context)

#student
def student_list(request):
    query = request.GET.get('q', '').strip()
    status_filter = request.GET.get('status', 'Active').strip()
    students = Students.objects.all().order_by('-student_id')
    if status_filter.lower() == 'active':
        students = students.filter(status__iexact='Active')
        status_filter = 'Active'
    elif status_filter.lower() == 'inactive':
        students = students.filter(status__iexact='Inactive')
        status_filter = 'Inactive'
    else:
        status_filter = 'all'
    if query:
        students = students.filter(
            Q(student_number__icontains=query) |
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query)|
            Q(phone__icontains=query)
        )
    return render(request, 'core/student_list.html', {
        'students': students,
        'query': query,
        'status_filter': status_filter})
def student_detail(request,student_id):
    student = get_object_or_404(Students, student_id = student_id)
    context = {
        'student': student}
    return render(request,'core/student_detail.html', context)
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        
        if form.is_valid():

           student = form.save()

           parent = form.cleaned_data.get('parent')
           if parent:
                relationship = form.cleaned_data.get('relationship') or 'Father'
                isprimary = form.cleaned_data.get('isprimary',True)
                isemergencycontact = form.cleaned_data.get('isemergencycontact' , True)

                StudentParents.objects.create(
                    student=student,
                    parent=parent,
                    relationship=relationship,
                    isprimary=isprimary,
                    isemergencycontact=isemergencycontact
                )

                return redirect('student_list')
        else:
            print("----erorr----")
            print(form.errors)
    else:
        form = StudentForm()

   
    return render(request, 'core/student_form.html', {'form': form})


def student_edit(request, student_id):
    student = get_object_or_404(Students, student_id=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_detail', student_id=student.student_id)
    else:
        form = StudentForm(instance=student)
    return render(request, 'core/student_form.html', {'form': form, 'title': 'ویرایش اطلاعات شاگرد'})
    
def student_delete(request, student_id):
    student = get_object_or_404(Students, student_id=student_id)
    if request.method == 'POST':
        student.status='InActive'
        student.save()
        return redirect('student_list')
    return render(request, 'core/student_confirm_delete.html', {'student': student})
#qiuck parent
def quick_parent_create(request):
    if request.method =='POST':
        first_name = request.POST.get('first_name','').strip()
        last_name = request.POST.get('last_name','').strip()
        phone = request.POST.get('phone','').strip()
        email = request.POST.get('email','').strip()
        address = request.POST.get('address','').strip()


        if first_name and last_name and phone:
            parent = Parents.objects.create(
                first_name = first_name,
                last_name = last_name,
                email = email,
                address = address,
                phone = phone,

                isactive = True
            )
        return JsonResponse({
            'success': True,
            'id': parent.pk,
            'text':f"{parent.first_name} {parent.last_name} ({parent.phone})"
        })
    else:
        return JsonResponse({'success':False,'error':'لطفا تمام فیلد ها را پر کنید'},status=400)
    return JsonResponse({'success':False, 'error':'در خواست نا معتبر است'},status=400)


#teater list
def teacher_list(request):
    query = request.GET.get('q', '').strip()
    status_filter = request.GET.get('status', '').strip()
    teachers = Teachers.objects.all()
    if status_filter:
        if status_filter.lower() == 'active':
            teachers = teachers.filter(Q(status__iexact='Active') | Q(status='فعال'))
        elif status_filter.lower() == 'inactive':
            teachers = teachers.filter(Q(status__iexact='Inactive') | Q(status='غیرفعال'))
    if query:
        teachers = teachers.filter(
            Q(employee_number__icontains=query) |
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(national_id__icontains=query) |
            Q(phone__icontains=query)
        )
    return render(request, 'core/teacher_list.html', {
        'teachers': teachers,
        'query': query,
        'status_filter': status_filter
    })
    teachers = Teachers.objects.all().order_by('-teacher_id')
    return render(request, 'core/teacher_list.html',{'teachers':teachers})
def teacher_create(requset):
    if requset.method == 'POST':
        form = TeacherForm(requset.POST)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
    else:
        form = TeacherForm()
    return render(requset,'core/teacher_form.html',{'form':form,'tital':'ثبت استاد جدید'})
def teacher_edit(requset, teacher_id):
    teacher = get_object_or_404(Teachers,teacher_id = teacher_id)
    if requset.method == 'POST':
        form = TeacherForm(requset.POST, instance = teacher)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
    else:
        form = TeacherForm(instance = teacher)
    return render(requset,'core/teacher_form.html',{'form':form,'tital':'نمایش اطلاعات استاد'})
def teacher_delete(requset, teacher_id):
    teacher = get_object_or_404(Teachers,teacher_id = teacher_id)
    if requset.method == 'POST':
        teacher.status='InActive'
        teacher.save()
        return redirect('teacher_list')
    return render(requset, 'core/teacher_confirm_delete.html', {'teacher': teacher})

#classes
def class_list(request):
    query = request.GET.get('q','').strip()
    classes = Classes.objects.all().order_by('grade_level','class_name')
    if query:
        classes = classes.filter(
            Q(class_name__icontains=query)|Q(grade_level__icontains=query))
    return render(request, 'core/class_list.html', {
        'classes': classes,
        'query': query
    })
def class_create(request):
    if request.method == 'POST':
        form = ClassForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('class_list')
    else:
        form = ClassForm()
    return render(request, 'core/class_form.html', {'form': form, 'title': 'ثبت صنف جدید'})
def class_edit(request, class_id):
    single_class = get_object_or_404(Classes, class_id=class_id)
    if request.method == 'POST':
        form = ClassForm(request.POST, instance=single_class)
        if form.is_valid():
            form.save()
            return redirect('class_list')
    else:
        form = ClassForm(instance=single_class)
    return render(request, 'core/class_form.html', {'form': form, 'title': 'ویرایش اطلاعات صنف'})
def class_delete(request, class_id):
    single_class = get_object_or_404(Classes, class_id=class_id)
    if request.method == 'POST':
        single_class.delete()
        return redirect('class_list')
    return render(request, 'core/class_confirm_delete.html', {'class_obj': single_class})
#parents
def parent_list(request):
    query = request.GET.get('q', '').strip()
    student_parents = StudentParents.objects.select_related('parent', 'student').all().order_by('-student_parent_id')

    if query:
        student_parents = student_parents.filter(
            Q(parent__first_name__icontains=query) |
            Q(parent__last_name__icontains=query) |
            Q(parent__phone__icontains=query) |
            Q(student__first_name__icontains=query) |
            Q(student__last_name__icontains=query)
        )

    return render(request, 'core/parent_list.html', {
        'student_parents': student_parents,
        'query': query
    })
def parent_create(request):
    if request.method == 'POST':
        p_form = ParentForm(request.POST)
        sp_form = StudentParentForm(request.POST)
        if p_form.is_valid() and sp_form.is_valid():
            parent_obj = p_form.save()
            student_parent_obj = sp_form.save(commit=False)
            student_parent_obj.parent = parent_obj
            student_parent_obj.save()
            return redirect('parent_list')
    else:
        p_form = ParentForm()
        sp_form = StudentParentForm()

    return render(request, 'core/parent_form.html', {
        'p_form': p_form,
        'sp_form': sp_form,
        'title': 'ثبت ولی / سرپرست جدید'
    })

def parent_edit(request, parent_id):
    student_parent = get_object_or_404(StudentParents, student_parent_id=parent_id)
    parent = student_parent.parent

    if request.method == 'POST':
        p_form = ParentForm(request.POST, instance=parent)
        sp_form = StudentParentForm(request.POST, instance=student_parent)
        if p_form.is_valid() and sp_form.is_valid():
            p_form.save()
            sp_form.save()
            return redirect('parent_list')
    else:
        p_form = ParentForm(instance=parent)
        sp_form = StudentParentForm(instance=student_parent)

    return render(request, 'core/parent_form.html', {
        'p_form': p_form,
        'sp_form': sp_form,
        'title': 'ویرایش اطلاعات ولی / سرپرست'
    })

def parent_delete(request, parent_id):
    student_parent = get_object_or_404(StudentParents, student_parent_id=parent_id)
    if request.method == 'POST':
        parent = student_parent.parent
        student_parent.delete()
        parent.delete()
        return redirect('parent_list')
    return render(request, 'core/parent_confirm_delete.html', {'student_parent': student_parent})

def send_notification_to_parent( parent, title, message, notif_type='Attendance', channel = 'SMS'):
    notification = notification.objects.create(
    title = title,
    message = message,
    notificationtype = notif_type,
    createdat=timezone.now()
    )
    recipient = NotificationRecipients .objects.create(
    notification = notification,
    parent = parent,
    channel = channel,
    deliverystatus = 'Panding',
    createdat = timezone.now()
    )
#send_whatsapp_api(parent.phone,message)
    #recipient.deliverystatus = 'Send'
    #recipient.deliveredat = timezone.now()
    #recipient.save()
    return notification

def notification_list(request):
    query = request.GET.get('q','').strip()
    type_filter = request.GET.get('type','').strip()
    recipients = NotificationRecipients .objects.select_related('notification','parent').all().order_by('-createdat')

    if type_filter:
        recipients = recipients.filter(notification__notificationtype=type_filter)

    if query:
        recipients = recipients.filter(
            Q(notification_title_icontains=query) |
            Q(notification_message_icontains=query) |
            Q(parent_first_name_icontains=query) |
            Q(parent_last_name_icontains=query) |
            Q(parent_phone_icontains=query)
        )
    return render(request, 'core/notification_list.html', {
        'recipients': recipients,
        'query': query,
        'type_filter': type_filter,
    })
# ۲. ارسال اعلان عمومی 
def notification_create(request):
    if request.method == 'POST':
        form = Notification_form(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            message = form.cleaned_data['message']
            notif_type = form.cleaned_data['notificationtype']
            channel = form.cleaned_data['channel']
            target_class = form.cleaned_data['target_class']

            # ۱. ساخت اعلانات اصلی
            notification = Notifications.objects.create(
                title=title,
                message=message,
                notificationtype=notif_type,
                created_at=timezone.now()
            )
            # ۲. پیدا کردن والدین 
            if target_class:
                student_parents = StudentParents.objects.filter(
                    student__class_field=target_class
                ).select_related('parent')
                parents = [sp.parent for sp in student_parents if sp.parent]
            else:
                parents = Parents.objects.filter(isactive=True)
            # ۳. ایجاد لیست گیرندگان
            recipient_objects = []
            for parent in set(parents):
                recipient_objects.append(
                    NotificationRecipients(
                        notification=notification,
                        parent=parent,
                        channel=channel,
                        deliverystatus='Sent', # یا 'Pending'
                        deliveredat=timezone.now(),
                        createdat=timezone.now(),
                        isread=False
                    )
                )
            NotificationRecipients.objects.bulk_create(recipient_objects)
            return redirect('notification_list')
    else:
        form = Notification_form()

    return render(request, 'core/notification_form.html', {'form': form, 'title': 'ارسال اعلان جدید'})


#============== attandance========= notification
# در فایل core/views.py و داخل View ثبت حاضری/ورود و خروج:

def record_attendance(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    status = request.POST.get('status') # مثلاً 'Present', 'Absent', 'Entry', 'Exit
    time_str = timezone.now().strftime("%H:%M")

    student_parent = StudentParents.objects.filter(student=student).first()
    if student_parent and student_parent.parent:
        parent = student_parent.parent
        
        if status == 'Entry':
            title = "اطلاع‌رسانی ورود به مکتب"
            message = f"والدین گرامی؛ فرزند شما {student.first_name} در ساعت {time_str} وارد مکتب گردید."
        elif status == 'Exit':
            title = "اطلاع‌رسانی خروج از مکتب"
            message = f"والدین گرامی؛ فرزند شما {student.first_name} در ساعت {time_str} از مکتب خارج شد."
        elif status == 'Absent':
            title = "اطلاعیه غیبت"
            message = f"والدین گرامی؛ فرزند شما {student.first_name} امروز در مکتب غیرحاضر می‌باشد."

        send_notification_to_parent(
            parent=parent,
            title=title,
            message=message,
            notif_type='Attendance',
            channel='WhatsApp' # یا 'SMS'
        )

    return redirect('attendance_list')


def fee_list(request):
    """لیست صورت‌حساب‌های فیس با فیلتر وضعیت و جستجوی نام شاگرد و صنف"""
    search_query = request.GET.get('q','')
    status_filter = request.GET.get('status','')

    fees = Fees.objects.select_related('enrollment__student', 'enrollment__class_field').all().order_by('-fee_id')

    if status_filter:
        fees = fees.filter(status=status_filter)

    # جستجو بر اساس نام، تخلص، ای دی شاگرد یا نام صنف
    if search_query:
        fees = fees.filter(
            Q(enrollment__student__first_name_icontains=search_query) |
            Q(enrollment__student__last_name_icontains=search_query) 
            
        )
    return render(request, 'core/fee_list.html',{
        'fees':fees,
        'search_query':search_query,
        'status_filter':status_filter
    })



def fee_create(request):
    """ثبت فیس جدید"""
    if request.method == 'POST':
        form = FeeForm(request.POST)
        if form.is_valid():

            fee = form.save(commit=False)
            valid_types = ['Monthly', 'Tuition', 'Admission', 'Transport', 'Trasport', 'Exam', 'Other']

            if not fee.feetype or fee.feetype not in valid_types:
                fee.feetype = 'Monthly'
            fee.status = 'Unpaid'

            if hasattr(fee, 'createdat') and not getattr(fee, 'createdat', None):
                fee.createdat = timezone.now()
            fee.save()

            messages.success(request, 'فیس با موفقیت ثبت شد.')
            return redirect('fee_list')
        else:
            print("form error : ",fee.errors)
    else:
        form = FeeForm()

    return render(request, 'core/fee_form.html', {'form': form, 'title': 'ثبت فیس جدید'})

def record_payment(request, fee_id):
    """ثبت دریافت پول (رسید) برای یک فیس مشخص"""
    fee = get_object_or_404(Fees, fee_id=fee_id)
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.fee = fee
            # payment.received_by_id = request.user.id
            # payment.createdat = timezone.now()
            # payment.save()
            user_obj = Users.objects.filter(user_name=request.user.username).first() or Users.objects.first()
            # payment.recived_by = user_obj
            # fee.status = 'Paid'
            fee.save()

            return redirect('fee_list')
    else:
        form = PaymentForm(initial={'payment_date': timezone.now().date()})
    
    return render(request, 'core/payment_form.html', {'form': form, 'fee': fee})

#student / enrollments
def student_enroll(request):
    """ ثبت کامل مشخصات شاگرد، پدر و شمولیت در صنف """
    if request.method == 'POST':
        student_form = StudentForm(request.POST, prefix='student')
        parent_form = ParentForm(request.POST, prefix='parent')
        enrollment_form = EnrollmentForm(request.POST, prefix='enroll')
        
        if student_form.is_valid() and parent_form.is_valid() and enrollment_form.is_valid():
            
            student = student_form.save(commit=False)
            if not getattr(student,'admission_date',None):
                student.admission_date = date.today()

            if hasattr(student,'createdat') and not getattr(student,'createdat',None):
                student.createdat = timezone.now()
            elif hasattr(student,'created_at')and not getattr(student,'created_at',None):
                student.created_at = timezone.now()
            if hasattr(student,'status'):
                student.status = 'Active'
            student.save()

            parent = parent_form.save(commit=False)
            parent.last_name = student.last_name
            parent.isactive = True
            parent.save()
            
            rel_type = parent_form.cleaned_data.get('relationship', 'Father')
            StudentParents.objects.create(
                student=student,
                parent=parent,
                relationship=rel_type,
                isprimary=True,
                isemergencycontact=True
            )
            
            enrollment = enrollment_form.save(commit=False)
            enrollment.student = student

            if hasattr(enrollment,'enrollment_date')and not getattr(enrollment,'enrollment_date',None):
                enrollment.enrollment_date = date.today()
            elif hasattr(enrollment,'enrollmentdate') and not getattr(enrollment,'enrollmentdate',None):
                enrollment.enrollmentdate = date.today()

            if hasattr(enrollment,'createdat')and not getattr(enrollment,'createdat',None):
                enrollment.createdat = timezone.now()
            elif hasattr(enrollment,'createdat') and not getattr(enrollment,'createdat',None):
                enrollment.createdat = timezone.now()


            if hasattr(enrollment,'status'):
                enrollment.status = 'Active'
            enrollment.save()

            messages.success(request, f"شاگرد {student.first_name} {student.last_name} با موفقیت ثبت نام شد.")
            return redirect('fee_list')
        else:
            messages.error(request, "اطلاعات وارد شده معتبر نیست. لطفاً خطاهای درون فرم را بررسی کنید.")
    else:
        student_form = StudentForm(prefix='student')
        parent_form = ParentForm(prefix='parent')
        enrollment_form = EnrollmentForm(prefix='enroll')

    return render(request, 'core/student_enroll.html', {
        'student_form': student_form,
        'parent_form': parent_form,
        'enrollment_form': enrollment_form
    })