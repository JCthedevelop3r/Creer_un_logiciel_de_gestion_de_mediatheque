from django.contrib import admin
from librarians.models_members import Member
from librarians.models_medias import Media
from librarians.models_borrowing import Borrowing


class MemberAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'place_of_birth', 'city_of_residence', 'phone_number', 'borrowings_number']


class MediaAdmin(admin.ModelAdmin):
    list_display = ['name', 'borrowing_date', 'available', 'borrowers_number', 'quantity']


class BorrowingAdmin(admin.ModelAdmin):
    list_display = ['id', 'member', 'media', 'borrowing_date']


admin.site.register(Member, MemberAdmin)
admin.site.register(Media, MediaAdmin)
admin.site.register(Borrowing, BorrowingAdmin)
