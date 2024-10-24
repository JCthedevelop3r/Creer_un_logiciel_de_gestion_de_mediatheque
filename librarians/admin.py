from django.contrib import admin
from librarians.models_members import Member
from librarians.models_medias import Media
from librarians.models_borrowing import Borrowing


class MemberAdmin(admin.ModelAdmin):
    list_display = ['user', 'get_user_email', 'date_of_birth', 'place_of_birth', 'city_of_residence', 'phone_number', 'borrowings_number']

    # Méthode pour afficher l'email de l'utilisateur lié
    def get_user_email(self, obj):
        return obj.user.email

    # Personnaliser l'en-tête de la colonne dans l'admin
    get_user_email.short_description = 'Email'


class MediaAdmin(admin.ModelAdmin):
    list_display = ['name', 'borrowing_date', 'available', 'borrowers_number', 'quantity']


class BorrowingAdmin(admin.ModelAdmin):
    list_display = ['id', 'member', 'media', 'borrowing_date']


admin.site.register(Member, MemberAdmin)
admin.site.register(Media, MediaAdmin)
admin.site.register(Borrowing, BorrowingAdmin)
