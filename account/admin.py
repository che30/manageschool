from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import Account
from student.models import Student
from courses.models import Course
from teacher.models import Teacher
from attendance.models import Attendance
from department.models import Department
from marks.models import Mark
# Register your models here.
class AccountAdmin(UserAdmin):
  list_display = ('email','username','date_joined','last_login','is_admin','is_staff')
  search_fields = ('email','username')
  readonly_fields = ('id', 'date_joined','last_login')
  filter_horizontal = ()
  list_filter = ()
  fieldsets = ()
admin.site.register(Account, AccountAdmin)
admin.site.register(Student)
admin.site.register(Attendance)
admin.site.register(Course)
admin.site.register(Department)
admin.site.register(Teacher)
admin.site.register(Mark)