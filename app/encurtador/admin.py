from django.contrib import admin
from app.encurtador.models import Urlsredirect, UrlLog

# Register your models here.
@admin.register(Urlsredirect)
class UrlRedirectAdmin(admin.ModelAdmin):
    list_display = ('destino', 'slug', 'criado_em', 'atualizado_em')\

@admin.register(UrlLog)
class UrlLogAdmin(admin.ModelAdmin):
    list_display = ('origem', 'criado_em', 'user_age', 'host', 'ip', 'url_redirect')

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

