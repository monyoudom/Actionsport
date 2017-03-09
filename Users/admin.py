from django.contrib import admin

from . import models

class PlaygroundAdmin(admin.ModelAdmin):
	fields = ('user', 'name_playground', 'descition_playground', 'kind_of_sport', 'Location_playground', 'review_playground')
	empty_value_display = 'unknown'

class EventAdmin(admin.ModelAdmin):
	fields = ields = ('playground', 'event_name', 'event_instructions', 'event_review','start_date','end_date')
class PasteventAdmin(admin.ModelAdmin):
	fields = ('playground', 'event_name','describetion')
	empty_value_display = 'unknown'



admin.site.register(models.Playground, PlaygroundAdmin)
admin.site.register(models.Event, EventAdmin)
admin.site.register(models.Pastevent,PasteventAdmin )

