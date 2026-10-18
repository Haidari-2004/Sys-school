from django import forms
from .models import Students,Teachers,Classes,Parents,StudentParents,Enrollments
from .models import Notifications,Fees, FeesPayments,AcademicYears
import datetime

STATUS_CHOICES = [
    ('Active', 'فعال'),
    ('Inactive', 'غیر فعال'),]

GENDER_CHOICES = [
    ('Male', 'مرد'),
    ('Female', 'زن'),]

RELATIONSHIP_CHOICES = [
    ('Father', 'پدر'),
    ('Mother', 'مادر'),
    ('Guardian', 'ولی / سرپرست'),
    ('Other', 'سایر'),]

class StudentForm(forms.ModelForm):
    parent = forms.ModelChoiceField(
        queryset = Parents.objects.filter(isactive = True),
        required = False,
        label = "انتخاب والد",
        widget = forms.Select(attrs={'class':'form-select search-select'})
    )
    relationship = forms.ChoiceField(
        choices=RELATIONSHIP_CHOICES,
        required = False,
        initial='Father',
        label ="نسبت با شاگرد",
        widget = forms.Select(attrs={'class':'form-select' })
    )
    isprimary = forms.BooleanField(
        required = False,
        initial = True,
        label = "سرپرست اصلی",
        widget = forms.CheckboxInput(attrs={'class':'form-check-input'})
    )
    isemergencycontact = forms.BooleanField(
        required=False,
        initial=True,
        label= "تماس اظـطراری"  ,
        widget = forms.CheckboxInput(attrs={'class':'form-check-input'})
        )
    class Meta:
        model = Students
        fields = ['student_number','first_name','last_name','gender','date_of_birth','admission_date','phone','status','address']
        widgets = {
            'student_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نمبر / ایدی شاگرد'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'اسم شاگرد'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'تخلص'}),
            'gender': forms.Select(choices=GENDER_CHOICES, attrs={'class': 'form-select'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'admission_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '07xxxxxxxx'}),
            'status': forms.Select(choices=STATUS_CHOICES, attrs={'class': 'form-select'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows':  2, 'placeholder': 'ادرس سکونت'}),
        }
        
class ParentForm(forms.ModelForm):
    class Meta:
        model = Parents
        fields = ['first_name', 'last_name', 'phone', 'email', 'address', 'isactive']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'تخلص'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'شماره تماس'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'example@email.com'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ' آدرس'}),
            'isactive': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
class StudentParentForm(forms.ModelForm):

    class Meta:
        model = StudentParents
        fields = ['student', 'relationship', 'isprimary', 'isemergencycontact']
        widgets = {
            'student': forms.Select(attrs={'class': 'form-select'}),
            'relationship': forms.Select(choices=RELATIONSHIP_CHOICES, attrs={'class': 'form-select'}),
            'isprimary': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'isemergencycontact': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['student'].queryset = Students.objects.all().order_by('-student_id')
        self.fields['student'].empty_label = "-- انتخاب شاگرد --"



























STATUS_CHOICE=[ ('Active','فعال'),('Inactive','غیر فعال'),]
class TeacherForm(forms.ModelForm):

    class Meta:
        model = Teachers
        fields = [
            'employee_number',
            'first_name',
            'last_name',
            'national_id',
            'phone',
            'email',
            'hire_date',
            'status'
        ]
        widgets = {
            'employee_number':forms.TextInput(attrs={'class':'form-control','placeholder':'شماره کارمندی'}),
            'first_name' : forms.TextInput(attrs={'class':'form-control','placeholder':'اسم استاد'}),
            'last_name' : forms.TextInput(attrs={'class':'form-control','placeholder':'تخلص'}),
            'national_id':forms.TextInput(attrs={'class':'form-control','placeholder':'نمبر تذکره'}),
            'phone' : forms.NumberInput(attrs={'class':'form-control','placeholder':'07xxxxxxxx'}),
            'email' : forms.TextInput(attrs={'class':'form-control','placeholder':'example@email.com'}),
            'hire_date' : forms.TextInput(attrs={'class':'form-control', 'type':'date'}),
            'status' : forms.Select(choices=STATUS_CHOICE, attrs={'class':'form-select'}),
        }
class ClassForm(forms.ModelForm):
    class Meta:
        model = Classes
        fields = ['class_name','grade_level']

        widgets = {
            'class_name' : forms.TextInput(attrs={'class':'form-control','placeholder':'الف ، ب ، دهم الف'}),
            'grade_level' : forms.NumberInput(attrs={'class':'form-control','placeholder':'درجه صنف'}),

        }



CHANNEL_CHOICES = [
    ('SMS','پیامک (SMS)'),
    ('Whatsapp','واتسپ (whatsapp)'),
    ('Both',' هردو( whatsapp + SMS)'),]
NOTIFICATION_TYPE_CHOICES = [
    ('attendance','اطلاعیه حاضری'),  
    ('announcement','اطلاعیه عمومی') ,
    ('fee','یاد آوری فیس') ,
]
class Notification_form(forms.ModelForm):
    channel = forms.ChoiceField(
        choices = CHANNEL_CHOICES,
        widget = forms.Select(attrs = {'class':'form-select'}),
        label = 'ارسال کانال'
    )
    target_class = forms.ModelChoiceField(
        queryset = Classes.objects.all(),
        required = False,
        empty_label = '--همه والدین (تمام مکتب)--',
        widget=forms.Select(attrs={'class':'form-select'}),
        label= ' ارسال به صنف خاص' )
    notificationtype = forms.ChoiceField(
        choices=NOTIFICATION_TYPE_CHOICES,
        widget = forms.Select(attrs={'class':'form-select'}),
        label = 'نوع اعلان'
    )
    class Meta:
        model = Notifications
        fields = ['title','message','notificationtype']
        widget = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'عنوان اعلان'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows':4, 'placeholder': 'متن پیام اطلاعیه...'}),
            'notification': forms.Select(choices = NOTIFICATION_TYPE_CHOICES,attrs={'class': 'form-select'}),
        }
#fees


# لیست ماه‌های هجری شمسی
MONTH_CHOICES = [
    (1, 'حمل (ماه ۱)'),
    (2, 'ثور (ماه ۲)'),
    (3, 'جوزا (ماه ۳)'),
    (4, 'سرطان (ماه ۴)'),
    (5, 'اسد (ماه ۵)'),
    (6, 'سنبله (ماه ۶)'),
    (7, 'میزان (ماه ۷)'),
    (8, 'عقرب (ماه ۸)'),
    (9, 'قوس (ماه ۹)'),
    (10, 'جدی (ماه ۱۰)'),
    (11, 'دلو (ماه ۱۱)'),
    (12, 'حوت (ماه ۱۲)'),
]

FEE_STATUS_CHOICES = [
    ('Unpaid', 'پرداخت نشده'),
    ('Partial', 'قسمتی پرداخت شده'),
    ('Paid', 'پرداخت شده'),
]

CURRENCY_CHOICES = [
    ('AFN', 'افغانی (AFN)'),
    ('USD', 'دالر (USD)'),
]

class FeeForm(forms.ModelForm):
    enrollment = forms.ModelChoiceField(
        queryset=Enrollments.objects.select_related('student', 'class_field').all(),
        widget=forms.Select(attrs={'class ' :  'form-select select2'}),
        label='انتخاب شاگرد (همراه با صنف)'
    )
    fee_month = forms.ChoiceField(
        choices=MONTH_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='ماه مربوطه'
    )
    # status = forms.ChoiceField(
    #     choices=FEE_STATUS_CHOICES,
    #     widget=forms.Select(attrs={'class': 'form-select'}),
    #     label='وضعیت اولیه'
    # )
    currency = forms.ChoiceField(
        choices=CURRENCY_CHOICES,
        initial='AFN',
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='واحد پول'
    )
    discount_amount = forms.DecimalField(
        required=False,
        initial=0,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        label='مبلغ تخفیف'
    )
    class Meta:
        model = Fees
        fields = ['enrollment', 'feetype', 'fee_month', 'amount', 'discount_amount', 'currency', 'due_date', 'description']
        labels = {
            'feetype': 'نوع فیس',
            'amount': 'مبلغ اصلی',
            'due_date': 'تاریخ سررسید',
            'description': 'توضیحات',
        }
        widgets = {
            'feetype': forms.Select(choices=Fees.FEE_TYPE_CHOICES, attrs={'class': 'form-select'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'due_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # نمایش کامل نام شاگرد + صنف در گزینه‌های ModelChoiceField
        self.fields['enrollment'].label_from_instance = lambda obj: f"{obj.student.first_name} {obj.student.last_name} — [صنف: {obj.class_field}] ({obj.student.student_number})"

class PaymentForm(forms.ModelForm):
    class Meta:
        model = FeesPayments
        fields = ['amount', 'payment_date', 'payment_method', 'receipt_number', 'reference_number', 'notes']
        labels = {
            'amount': 'مبلغ تحویلی',
            'payment_date': 'تاریخ پرداخت',
            'payment_method': 'روش پرداخت',
            'receipt_number': 'شماره رسید',
            'reference_number': 'شماره ارجاع / رفرنس',
            'notes': 'یادداشت',
        }
        widgets = {
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'payment_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'payment_method': forms.Select(choices=FeesPayments.PAYMENT_METHOD_CHOICE, attrs={'class': 'form-select'}),
            'receipt_number': forms.TextInput(attrs={'class': 'form-control'}),
            'reference_number': forms.TextInput(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }
#student == Enrollment

class ParentForm(forms.ModelForm):
    relationship = forms.ChoiceField(
        choices=RELATIONSHIP_CHOICES,
        widget = forms.Select(attrs={'class':'form-select'}),
        label = "نسبت قرابت"
    )

    class Meta:
        model = Parents
        fields = ['first_name','phone']
        widgets = {
            'first_name':forms.TextInput(attrs={'class': 'form-control', 'placeholder':'نام پدر / ولی'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'شماره تماس  ولی'}),
        }
        labels = {
            'first_name':'نام پدر / ولی',
            'phone':'شماره تماس ولی'
        }

class EnrollmentForm(forms.ModelForm):
    class_field = forms.ModelChoiceField(
        queryset = Classes.objects.all(),
        empty_label="--انتخاب صنف--",
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='انتخاب صنف'
    )
    academic_year = forms.ModelChoiceField(
        queryset = AcademicYears.objects.all(),
        empty_label="--انتخاب  سال تحصیلی--",
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='سال تحصیلی '   
    )
    class Meta:
        model = Enrollments
        fields = ['class_field','academic_year']
    # def __init__(self,*args,**kwargs):
    #     super().__init__(*args,**kwargs)

    #     existing_years = set(Enrollments.objects.values_list('academic_year',flat=True).distinct())

    #     valid_db_years = {str(y).strip() for y in existing_years if y and str(y).strip().isdigit() and len(str(y).strip())==4}

    #     auto_years = {str(y) for y in range(1405,1410)}
    #     all_years = sorted(list(valid_db_years | auto_years), reverse= True)

    #     self.fields['academic_year'].choices = [('','--انتخاب سال تحصیلی--')] + [(y , y) for y in all_years ]
        
        
