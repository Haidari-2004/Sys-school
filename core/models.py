from django.db import models

# Create your models here.
class AcademicYears(models.Model):
    academic_year_id = models.AutoField(db_column='Academic_year_id', primary_key=True)  # Field name made lowercase.
    year_name = models.CharField(db_column='Year_Name', unique=True, max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    start_date = models.DateField(db_column='Start_date')  # Field name made lowercase.
    end_date = models.DateField(db_column='End_Date')  # Field name made lowercase.
    iscurrent = models.BooleanField(db_column='IsCurrent', unique=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt')  # Field name made lowercase.
    def __str__(self):  
        return self.year_name

    class Meta:
        managed = False
        db_table = 'Academic_years'


class ActivityLog(models.Model):
    activity_log_id = models.AutoField(db_column='Activity_log_id', primary_key=True)  # Field name made lowercase.
    user = models.ForeignKey('Users', models.DO_NOTHING, db_column='User_id', blank=True, null=True)  # Field name made lowercase.
    action = models.CharField(db_column='Action', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    table_name = models.CharField(db_column='Table_name', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    record_id = models.IntegerField(db_column='Record_id', blank=True, null=True)  # Field name made lowercase.
    details = models.CharField(db_column='Details', max_length=1000, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Activity_log'


class Announcements(models.Model):
    announcement_id = models.AutoField(db_column='Announcement_id', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    message = models.CharField(db_column='Message', max_length=1000, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt')  # Field name made lowercase.
    created_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    ispublished = models.BooleanField(db_column='IsPublished')  # Field name made lowercase.
    publishedat = models.DateTimeField(db_column='PublishedAt', blank=True, null=True)  # Field name made lowercase.
    expiresat = models.DateTimeField(db_column='ExpiresAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Announcements'


class Assets(models.Model):
    asset_id = models.AutoField(db_column='Asset_id', primary_key=True)  # Field name made lowercase.
    asset_code = models.CharField(db_column='Asset_code', unique=True, max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    asset_name = models.CharField(db_column='Asset_name', max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    asset_category = models.CharField(db_column='Asset_Category', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    purchase_date = models.DateField(db_column='Purchase_Date', blank=True, null=True)  # Field name made lowercase.
    purchase_price = models.DecimalField(db_column='Purchase_price', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity')  # Field name made lowercase.
    condition = models.CharField(db_column='Condition', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    assigned_to = models.CharField(db_column='Assigned_to', max_length=120, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Assets'


class Attendance(models.Model):
    attendance_id = models.AutoField(db_column='Attendance_id', primary_key=True)  # Field name made lowercase.
    enrollment = models.ForeignKey('Enrollments', models.DO_NOTHING, db_column='Enrollment_id')  # Field name made lowercase.
    attendance_date = models.DateField(db_column='Attendance_Date')  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    check_intime = models.TimeField(db_column='Check_inTime', blank=True, null=True)  # Field name made lowercase.
    check_outtime = models.TimeField(db_column='Check_outTime', blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(db_column='Source', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    recorded_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='Recorded_by', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Attendance'
        unique_together = (('enrollment', 'attendance_date'),)


class ClassSchedules(models.Model):
    schedule_id = models.AutoField(db_column='Schedule_id', primary_key=True)  # Field name made lowercase.
    class_field = models.ForeignKey('Classes', models.DO_NOTHING, db_column='Class_id')  # Field name made lowercase. Field renamed because it was a Python reserved word.
    subject = models.ForeignKey('Subjects', models.DO_NOTHING, db_column='Subject_id')  # Field name made lowercase.
    teacher = models.ForeignKey('Teachers', models.DO_NOTHING, db_column='Teacher_id')  # Field name made lowercase.
    classroom = models.ForeignKey('ClassRooms', models.DO_NOTHING, db_column='Classroom_id', blank=True, null=True)  # Field name made lowercase.
    academic_year = models.ForeignKey(AcademicYears, models.DO_NOTHING, db_column='Academic_year_id')  # Field name made lowercase.
    term = models.ForeignKey('Terms', models.DO_NOTHING, db_column='Term_id')  # Field name made lowercase.
    day_of_week = models.SmallIntegerField(db_column='Day_of_Week')  # Field name made lowercase.
    start_time = models.TimeField(db_column='Start_time')  # Field name made lowercase.
    end_time = models.TimeField(db_column='End_time')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Class_Schedules'
        unique_together = (('class_field', 'class_field', 'class_field', 'subject', 'subject', 'subject', 'teacher', 'teacher', 'teacher', 'academic_year', 'academic_year', 'academic_year', 'academic_year', 'term', 'day_of_week', 'start_time', 'end_time'),)


class ClassSubjects(models.Model):
    class_subject_id = models.AutoField(db_column='Class_subject_id', primary_key=True)  # Field name made lowercase.
    class_field = models.ForeignKey('Classes', models.DO_NOTHING, db_column='Class_id')  # Field name made lowercase. Field renamed because it was a Python reserved word.
    subject = models.ForeignKey('Subjects', models.DO_NOTHING, db_column='Subject_id')  # Field name made lowercase.
    academic_year = models.ForeignKey(AcademicYears, models.DO_NOTHING, db_column='Academic_year_id')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Class_Subjects'
        unique_together = (('class_field', 'subject', 'academic_year'),)


class ClassRooms(models.Model):
    class_room_id = models.AutoField(db_column='Class_room_id', primary_key=True)  # Field name made lowercase.
    room_name = models.CharField(db_column='Room_name', unique=True, max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    capacity = models.IntegerField(db_column='Capacity', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Class_rooms'


class Classes(models.Model):
    class_id = models.AutoField(db_column='Class_id', primary_key=True)  # Field name made lowercase.
    class_name = models.CharField(db_column='Class_name', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS') # Field name made lowercase.
    grade_level = models.IntegerField(db_column='Grade_level')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt' ,auto_now_add=True)  # Field name made lowercase.
    def __str__(self): return self.class_name 

    class Meta:
        managed = False
        db_table = 'Classes'
        unique_together = (('grade_level', 'class_name'),)


class EmergencyContacts(models.Model):
    emergency_contact_id = models.AutoField(db_column='Emergency_contact_id', primary_key=True)  # Field name made lowercase.
    student = models.ForeignKey('Students', models.DO_NOTHING, db_column='Student_id')  # Field name made lowercase.
    first_name = models.CharField(db_column='First_name', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    last_name = models.CharField(db_column='Last_name', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    relationship = models.CharField(db_column='Relationship', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    isprimary = models.BooleanField(db_column='IsPrimary')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Emergency_contacts'


class Enrollments(models.Model):
    enrollment_id = models.AutoField(db_column='Enrollment_id', primary_key=True)  # Field name made lowercase.
    student = models.ForeignKey('Students', models.DO_NOTHING, db_column='Student_id')  # Field name made lowercase.
    class_field = models.ForeignKey(Classes, models.DO_NOTHING, db_column='Class_id')  # Field name made lowercase. Field renamed because it was a Python reserved word.
    academic_year = models.ForeignKey(AcademicYears, models.DO_NOTHING, db_column='Academic_year_id')  # Field name made lowercase.
    enrollment_date = models.DateField(db_column='Enrollment_date')  # Field name made lowercase.
    end_date = models.DateField(db_column='End_date', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    roll_number = models.CharField(db_column='Roll_number', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', )  # Field name made lowercase.
    def __str__(self): return f"{self.student}-{self.class_field} ({self.academic_year})"
    class Meta:
        managed = False
        db_table = 'Enrollments'
        unique_together = (('student', 'academic_year'), ('class_field', 'academic_year', 'roll_number'),)


class ExamSubjects(models.Model):
    exam_subject_id = models.AutoField(db_column='Exam_subject_id', primary_key=True)  # Field name made lowercase.
    exam = models.ForeignKey('Exams', models.DO_NOTHING, db_column='Exam_id')  # Field name made lowercase.
    subject = models.ForeignKey('Subjects', models.DO_NOTHING, db_column='Subject_id')  # Field name made lowercase.
    exam_date = models.DateField(db_column='Exam_date')  # Field name made lowercase.
    max_score = models.DecimalField(db_column='Max_score', max_digits=7, decimal_places=2)  # Field name made lowercase.
    pass_score = models.DecimalField(db_column='Pass_score', max_digits=7, decimal_places=2)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Exam_Subjects'
        unique_together = (('exam', 'subject'),)


class Exams(models.Model):
    exam_id = models.AutoField(db_column='Exam_id', primary_key=True)  # Field name made lowercase.
    exam_name = models.CharField(db_column='Exam_name', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    exam_type = models.CharField(db_column='Exam_type', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    term = models.ForeignKey('Terms', models.DO_NOTHING, db_column='Term_id')  # Field name made lowercase.
    class_field = models.ForeignKey(Classes, models.DO_NOTHING, db_column='Class_id')  # Field name made lowercase. Field renamed because it was a Python reserved word.
    start_date = models.DateField(db_column='Start_date')  # Field name made lowercase.
    end_date = models.DateField(db_column='End_date')  # Field name made lowercase.
    ispublished = models.BooleanField(db_column='IsPublished')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Exams'
        unique_together = (('class_field', 'term', 'exam_name'), ('class_field', 'term'), ('class_field', 'term'),)


class ExamsResults(models.Model):
    exam_result_id = models.AutoField(db_column='Exam_result_id', primary_key=True)  # Field name made lowercase.
    exam_subject = models.ForeignKey(ExamSubjects, models.DO_NOTHING, db_column='Exam_subject_id')  # Field name made lowercase.
    enrollment = models.ForeignKey(Enrollments, models.DO_NOTHING, db_column='Enrollment_id')  # Field name made lowercase.
    score = models.DecimalField(db_column='Score', max_digits=7, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    recorded_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='Recorded_by', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Exams_Results'
        unique_together = (('exam_subject', 'enrollment'),)


class Expenses(models.Model):
    expenses_id = models.AutoField(db_column='Expenses_id', primary_key=True)  # Field name made lowercase.
    expenses_title = models.CharField(db_column='Expenses_title', max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=12, decimal_places=2)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    expense_date = models.DateField(db_column='Expense_date')  # Field name made lowercase.
    payment_method = models.CharField(db_column='Payment_method', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    payee = models.CharField(db_column='Payee', max_length=120, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    reference_number = models.CharField(db_column='Reference_Number', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    recorded_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='Recorded_by', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Expenses'


class Fees(models.Model):
    fee_id = models.AutoField(db_column='Fee_id', primary_key=True)  # Field name made lowercase.
    enrollment = models.ForeignKey(Enrollments, models.DO_NOTHING, db_column='Enrollment_id')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=12, decimal_places=2)  # Field name made lowercase.
    discount_amount = models.DecimalField(db_column='Discount_amount', max_digits=12, decimal_places=2)  # Field name made lowercase.
    description = models.CharField(db_column='Description', 
    max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    fee_month = models.SmallIntegerField(db_column='Fee_Month', blank=True, null=True)  # Field name made lowercase.
    FEE_TYPE_CHOICES = [('Monthly','ماهوار'),
                        ('Tuition','فیس تدریسی'),
                        ('Admission','فیس داخله'), 
                        ('Transport','ترانسپورت'),
                        ('Exam','فیس امتحان'),
                        ('Other','سایر موارد'), ]
    feetype = models.CharField(db_column='FeeType', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS',choices =FEE_TYPE_CHOICES)  # Field name made lowercase.
    due_date = models.DateField(db_column='Due_date')  # Field name made lowercase.
    currency = models.CharField(db_column='Currency', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', auto_now_add=True)  # Field name made lowercase.
   
    def __str__(self):
        return f"fees{self.enrollment.student.first_name}{self.enrollment.student.last_name}-{self.feetype}({self.amount})"
    class Meta:
        managed = False
        db_table = 'Fees'
        unique_together = (('enrollment', 'fee_month', 'feetype'),)


class FeesPayments(models.Model):
    PAYMENT_METHOD_CHOICE = [('Cash','Cash'), ('Bank Transfer', 'Bank Transfer'),('Card','Card'),]
    payment_id = models.AutoField(db_column='Payment_id', primary_key=True)  # Field name made lowercase.
    fee = models.ForeignKey(Fees, models.DO_NOTHING)
    amount = models.DecimalField(db_column='Amount', max_digits=12, decimal_places=2)  # Field name made lowercase.
    payment_date = models.DateField(db_column='Payment_date')  # Field name made lowercase.
    payment_method = models.CharField(max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', choices=PAYMENT_METHOD_CHOICE)
    reference_number = models.CharField(db_column='Reference_Number', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    receipt_number = models.CharField(db_column='Receipt_Number', unique=True, max_length=80, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    received_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='Received_by', blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', auto_now_add=True)  # Field name made lowercase.
    def __str__(self): 
        return f"({self.student_number}) {self.first_name}{self.last_name}"
    
    def __str__(self):
        return f"رسید{self.receipt_number}-مبلغ:{self.payment_method}"
    
    class Meta:
        managed = False
        db_table = 'Fees_payments'

class NotificationRecipients(models.Model):
    notification_recipient_id = models.AutoField(db_column='Notification_recipient_id', primary_key=True)  # Field name made lowercase.
    notification = models.ForeignKey('Notifications', models.DO_NOTHING, db_column='Notification_id')  # Field name made lowercase.
    parent = models.ForeignKey('Parents', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, db_column='User_id', blank=True, null=True)  # Field name made lowercase.
    channel = models.CharField(db_column='Channel', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    deliverystatus = models.CharField(db_column='DeliveryStatus', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    deliveredat = models.DateTimeField(db_column='DeliveredAt', blank=True, null=True)  # Field name made lowercase.
    isread = models.BooleanField(db_column='IsRead')  # Field name made lowercase.
    readat = models.DateTimeField(db_column='ReadAt', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt',auto_now_add=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Notification_recipients'
        unique_together = (('notification', 'parent', 'channel'), ('notification', 'user', 'channel'),)

class Notifications(models.Model):
    notification_id = models.AutoField(db_column='Notification_id', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    message = models.CharField(db_column='Message', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    notificationtype = models.CharField(db_column='NotificationType', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    created_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField(db_column='Created_At',auto_now_add=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Notifications'


class Parents(models.Model):
    parent_id = models.AutoField(db_column='Parent_id', primary_key=True)  # Field name made lowercase.
    first_name = models.CharField(db_column='First_name', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    last_name = models.CharField(db_column='Last_name', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt',auto_now_add=True)  # Field name made lowercase.
    def __str__(self): 
        return f"({self.first_name}) {self.last_name}{self.phone}"

    class Meta:
        managed = False
        db_table = 'Parents'


class Salaries(models.Model):
    salary_id = models.AutoField(db_column='Salary_id', primary_key=True)  # Field name made lowercase.
    teacher = models.ForeignKey('Teachers', models.DO_NOTHING, db_column='Teacher_id', blank=True, null=True)  # Field name made lowercase.
    staff = models.ForeignKey('Staff', models.DO_NOTHING, db_column='Staff_id', blank=True, null=True)  # Field name made lowercase.
    salary_month = models.SmallIntegerField(db_column='Salary_month')  # Field name made lowercase.
    salary_year = models.SmallIntegerField(db_column='Salary_year')  # Field name made lowercase.
    base_amount = models.DecimalField(db_column='Base_amount', max_digits=12, decimal_places=2)  # Field name made lowercase.
    bonus_amount = models.DecimalField(db_column='Bonus_amount', max_digits=12, decimal_places=2)  # Field name made lowercase.
    deduction_amount = models.DecimalField(db_column='Deduction_amount', max_digits=12, decimal_places=2)  # Field name made lowercase.
    payment_status = models.CharField(db_column='Payment_status', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    payment_date = models.DateField(db_column='Payment_date', blank=True, null=True)  # Field name made lowercase.
    payment_method = models.CharField(db_column='Payment_method', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    reference_number = models.CharField(db_column='Reference_Number', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    recorded_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='Recorded_by', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Salaries'
        unique_together = (('teacher', 'salary_year', 'salary_month'), ('staff', 'salary_year', 'salary_month'),)


class Staff(models.Model):
    staff_id = models.AutoField(db_column='Staff_id', primary_key=True)  # Field name made lowercase.
    employee_number = models.CharField(db_column='Employee_number', unique=True, max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    first_name = models.CharField(db_column='First_name', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    last_name = models.CharField(db_column='Last_name', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    email = models.CharField(db_column='Email', unique=True, max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    position = models.CharField(db_column='Position', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    national_id = models.CharField(db_column='National_id', unique=True, max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    hire_date = models.DateField(db_column='Hire_date', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Staff'


class StudentParents(models.Model):
    student_parent_id = models.AutoField(db_column='Student_parent_id', primary_key=True)  # Field name made lowercase.
    student = models.ForeignKey('Students', models.DO_NOTHING, db_column='Student_id')  # Field name made lowercase.
    parent = models.ForeignKey(Parents, models.DO_NOTHING, db_column='Parent_id')  # Field name made lowercase.
    relationship = models.CharField(db_column='Relationship', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    isprimary = models.BooleanField(db_column='IsPrimary')  # Field name made lowercase.
    isemergencycontact = models.BooleanField(db_column='IsEmergencyContact')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt',auto_now_add=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Student_parents'
        unique_together = (('student', 'parent'),)


class Students(models.Model):
    student_id = models.AutoField(db_column='Student_id', primary_key=True)  # Field name made lowercase.
    student_number = models.CharField(db_column='Student_number', unique=True, max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    first_name = models.CharField(db_column='First_name', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    last_name = models.CharField(db_column='Last_name', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    date_of_birth = models.DateField(db_column='Date_of_birth', blank=True, null=True)  # Field name made lowercase.
    GENDER_CHOICES  = [('Male','Male'),('Female','Female'),]
    gender =  models.CharField(db_column='Gender', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS' ,choices = GENDER_CHOICES )  # Field name made lowercase.
    admission_date = models.DateField(db_column='Admission_date')  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt',auto_now_add=True)  # Field name made lowercase.
    def __str__(self): 
        return f"({self.student_number}) {self.first_name}{self.last_name}"

    class Meta:
        managed = False
        db_table = 'Students'


class Subjects(models.Model):
    subject_id = models.AutoField(db_column='Subject_id', primary_key=True)  # Field name made lowercase.
    subject_code = models.CharField(db_column='Subject_code', unique=True, max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    subject_name = models.CharField(db_column='Subject_name', unique=True, max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Subjects'


class TeacherClasses(models.Model):
    teacher_class_id = models.AutoField(db_column='Teacher_Class_id', primary_key=True)  # Field name made lowercase.
    teacher = models.ForeignKey('Teachers', models.DO_NOTHING, db_column='Teacher_id')  # Field name made lowercase.
    class_field = models.ForeignKey(Classes, models.DO_NOTHING, db_column='Class_id')  # Field name made lowercase. Field renamed because it was a Python reserved word.
    academic_year = models.ForeignKey(AcademicYears, models.DO_NOTHING, db_column='Academic_year_id')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Teacher_Classes'
        unique_together = (('teacher', 'class_field', 'academic_year'),)


class TeacherSubjects(models.Model):
    teachersubject_id = models.AutoField(db_column='TeacherSubject_id', primary_key=True)  # Field name made lowercase.
    teacher = models.ForeignKey('Teachers', models.DO_NOTHING, db_column='Teacher_id')  # Field name made lowercase.
    subject = models.ForeignKey(Subjects, models.DO_NOTHING, db_column='Subject_id')  # Field name made lowercase.
    academic_year = models.ForeignKey(AcademicYears, models.DO_NOTHING, db_column='Academic_year_id')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Teacher_Subjects'
        unique_together = (('teacher', 'subject', 'academic_year'),)
        
class Teachers(models.Model):
    
    teacher_id = models.AutoField(db_column='Teacher_id', primary_key=True)  # Field name made lowercase.
    employee_number = models.CharField(db_column='Employee_number', unique=True, max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    first_name = models.CharField(db_column='First_name', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    last_name = models.CharField(db_column='Last_name', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    national_id = models.CharField(db_column='National_id', unique=True, max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', unique=True, max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    hire_date = models.DateField(db_column='Hire_date', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS',)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt',auto_now_add=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Teachers'


class Terms(models.Model):
    term_id = models.AutoField(db_column='Term_id', primary_key=True)  # Field name made lowercase.
    academic_year = models.ForeignKey(AcademicYears, models.DO_NOTHING, db_column='Academic_year_id')  # Field name made lowercase.
    term_name = models.CharField(db_column='Term_name', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    term_number = models.SmallIntegerField(db_column='Term_number')  # Field name made lowercase.
    start_date = models.DateField(db_column='Start_date')  # Field name made lowercase.
    end_date = models.DateField(db_column='End_date')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Terms'
        unique_together = (('academic_year', 'term_name'), ('academic_year', 'term_number'),)


class Users(models.Model):
    user_id = models.AutoField(db_column='User_id', primary_key=True)  # Field name made lowercase.
    user_name = models.CharField(db_column='User_name', unique=True, max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    password_hash = models.CharField(db_column='Password_Hash', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    role = models.CharField(db_column='Role', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
    first_name = models.CharField(db_column='First_name', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    last_name = models.CharField(db_column='Last_name', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    email = models.CharField(db_column='Email', unique=True, max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    teacher = models.OneToOneField(Teachers, models.DO_NOTHING, blank=True, null=True)
    staff = models.OneToOneField(Staff, models.DO_NOTHING, blank=True, null=True)
    parent = models.OneToOneField(Parents, models.DO_NOTHING, blank=True, null=True)
    createdat = models.DateTimeField(db_column='CreatedAt')  # Field name made lowercase.
    def __str__(self):
        return f"{self.first_name}{self.last_name}" if self.first_name else self.user_name


    class Meta:
        managed = False
        db_table = 'Users'


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128, db_collation='SQL_Latin1_General_CP1_CI_AS')
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysdiagrams'
        unique_together = (('principal_id', 'name'),)
