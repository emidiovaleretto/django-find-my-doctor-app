from django.contrib import admin
from .models import *


class ProfileAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ('user', 'role', 'birth',
                    'specialities_list', 'addresses_list')
    empty_value_display = 'Not provided'
    list_display_links = ('user', 'role')
    list_filter = ('user__is_active',)
    exclude = ('favorites', 'created_at', 'updated_at')
    readonly_fields = ('user',)
    search_fields = ('user__username',)
    fieldsets = (
        ('User', {
            'fields': ('user', 'birthday', 'image')
        }),
        ('Role', {
            'fields': ('role',)
        }),
        ('Extra', {
            'fields': ('specialities', 'addresses')
        }),
    )

    def birth(self, obj):
        if obj.birthday:
            return obj.birthday.strftime("%d/%m/%Y")

    def specialities_list(self, obj):
        return [i.name for i in obj.specialities.all()]

    def addresses_list(self, obj):
        return [i.name for i in obj.addresses.all()]

    class Media:
        css = {
            'all': ('css/style.css',)
        }
        js = ('js/script.js',)


admin.site.register(Profile, ProfileAdmin)
admin.site.register(County)
admin.site.register(District)
admin.site.register(Neighborhood)
admin.site.register(Address)
admin.site.register(DayWeek)
admin.site.register(Rating)
admin.site.register(Speciality)
