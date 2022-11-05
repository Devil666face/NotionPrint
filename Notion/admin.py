from pyexpat import model
from django import forms
from django.contrib import admin
from .models import Task, Typing
from django.utils.safestring import mark_safe
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from Notion.views import get_weekday

class TaskAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Task
        fields = '__all__'

class TaskAdmin(admin.ModelAdmin):
    form = TaskAdminForm
    list_display = ('title',
                    # 'content',
                    'appoint_to',
                    'get_week_day',
                    # 'photo',
                    'get_photo',
                    'active',
                    'typing',)
    list_display_links = ('title',)
    search_fields = ('title','content','appoint_to')
    list_editable = ('appoint_to','active','typing')#'photo',
    list_filter = ('active','typing','appoint_to')
    fields = ('title',
            'content',
            'appoint_to',
            'get_week_day',
            'photo',
            'get_photo',
            'typing',)
    readonly_fields = ('get_week_day','get_photo','created_at','update_at')
    # save_on_top = True


    def get_photo(self, obj):
        return mark_safe(f'<img src="{obj.photo.url}" width="250">') if obj.photo else ''

    def get_week_day(self, obj):
        return mark_safe(f"<p>{get_weekday(str(obj.appoint_to))}</p>")

    get_photo.short_description = 'Прикрепленное фото'
    get_week_day.short_description = 'День недели'


class TypingAdmin(admin.ModelAdmin):
    search_fields = ('title',)


admin.site.register(Task, TaskAdmin)
admin.site.register(Typing, TypingAdmin)

# admin.sites.AdminSite.site_title = ''
# admin.sites.AdminSite.site_header = ''
# admin.sites.AdminSite.index_title = 'Главная'