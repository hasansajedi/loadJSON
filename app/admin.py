from django.contrib import admin
from django.contrib.auth.models import User

from app.models import EmailModel


class EmailAdmin(admin.ModelAdmin):
    list_display = ['id_got', 'title', 'description', 'imageUrl']

    class Meta:
        model = EmailModel

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super().save_model(request, obj, form, change)


admin.site.register(EmailModel, EmailAdmin)
