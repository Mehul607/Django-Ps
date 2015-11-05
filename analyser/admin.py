from django.contrib import admin
from .models import Language, Colour, Sentence, Word

class LangAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Languages Registered', {'fields': ['language']}),
        ('Colour', {'fields': ['colour']}),
    ]
    list_display = ('language', 'colour')
    search_fields=["language"]

class SentenceAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Input', {'fields': ['stext']}),
    ]
class WordAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Input', {'fields': ['wtext']}),
    ]
    list_display = ('wtext', 'Language_Detected', 'Colour_Associated')
    def Language_Detected(self, object):
        return object.lang.language
    def Colour_Associated(self,object):
        return object.lang.colour.col

class ColourAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Colour', {'fields': ['col']}),
        ('Hash', {'fields': ['hashcode']}),
    ]
    list_display = ('col', 'hashcode', )

admin.site.register(Language, LangAdmin)
admin.site.register(Colour,ColourAdmin)
admin.site.register(Word,WordAdmin)
admin.site.register(Sentence)
