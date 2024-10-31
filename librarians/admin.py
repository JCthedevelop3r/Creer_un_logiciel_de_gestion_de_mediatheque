from django.contrib import admin
from librarians.models_members import Member
from librarians.models_medias import Book
from librarians.models_medias import Cd
from librarians.models_medias import Board_game
from librarians.models_medias import Dvd
from librarians.models_borrowing import Borrowing


class MemberAdmin(admin.ModelAdmin):
    list_display = ['user', 'get_user_email', 'date_of_birth', 'place_of_birth', 'city_of_residence', 'phone_number',
                    'borrowings_number']

    # Méthode pour afficher l'email de l'utilisateur lié
    def get_user_email(self, obj):
        return obj.user.email

    # Personnaliser l'en-tête de la colonne dans l'admin
    get_user_email.short_description = 'Email'


class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'author', 'borrowing_date', 'available', 'borrowers_number', 'quantity']


class CdAdmin(admin.ModelAdmin):
    list_display = ['name', 'artist', 'borrowing_date', 'available', 'borrowers_number', 'quantity']


class BoardGameAdmin(admin.ModelAdmin):
    list_display = ['name', 'creator', 'available', 'quantity']


class DvdAdmin(admin.ModelAdmin):
    list_display = ['name', 'director', 'borrowing_date', 'available', 'borrowers_number', 'quantity']


class BorrowingAdmin(admin.ModelAdmin):
    list_display = ['id', 'member', 'media', 'borrowing_date', 'due_date']


admin.site.register(Member, MemberAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Cd, CdAdmin)
admin.site.register(Board_game, BoardGameAdmin)
admin.site.register(Dvd, DvdAdmin)
admin.site.register(Borrowing, BorrowingAdmin)
