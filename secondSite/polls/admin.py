from django.contrib import admin
from polls.models import Poll
from polls.models import Choice

class ChoiceInline(admin.TabularInline):
  model = Choice
  extra = 1

class PollAdmin(admin.ModelAdmin):
  fieldsets = [
    (None,               {'fields': ['question']}),
    ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),
  ]
  inlines = [ChoiceInline]

admin.site.register(Poll, PollAdmin)
