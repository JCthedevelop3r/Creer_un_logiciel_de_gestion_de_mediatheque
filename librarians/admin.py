from django.contrib import admin
from librarians.models_members import Member
from librarians.models_medias import Media


class MemberAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'place_of_birth', 'city_of_residence', 'phone_number', 'borrowings_number']


class MediaAdmin(admin.ModelAdmin):
    list_display = ['name', 'borrowing_date', 'available', 'borrowers_number', 'quantity']


admin.site.register(Member, MemberAdmin)
admin.site.register(Media, MediaAdmin)
