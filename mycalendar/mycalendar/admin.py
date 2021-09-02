from django.contrib import admin

from .models import User, Note, short,Project, Long_notes, deleted_notes, report_bugs

admin.site.register(User)
admin.site.register(Note)
admin.site.register(short)
admin.site.register(Project)
admin.site.register(Long_notes)
admin.site.register(deleted_notes)
admin.site.register(report_bugs)