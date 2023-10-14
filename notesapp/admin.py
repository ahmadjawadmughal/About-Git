from django.contrib import admin
# from notesapp.models import Note
from notesapp.models import Note

# Register your models here.
class NoteAdmin(admin.ModelAdmin):

    list_display = ["id","name","title","created_at"]
    search_fields = ["title","created_at"]
   # fields = ["name","title"]
   # exclude = ["content"]
    readonly_fields = ["title"]

admin.site.register(Note,NoteAdmin)