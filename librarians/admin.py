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

    # Personnalisation de l'en-tête de la colonne dans l'admin
    get_user_email.short_description = 'Email'


class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'author', 'borrowing_date', 'available', 'quantity']


class CdAdmin(admin.ModelAdmin):
    list_display = ['name', 'artist', 'borrowing_date', 'available', 'quantity']


class BoardGameAdmin(admin.ModelAdmin):
    list_display = ['name', 'creator', 'available', 'quantity']


class DvdAdmin(admin.ModelAdmin):
    list_display = ['name', 'director', 'borrowing_date', 'available', 'quantity']


class BorrowingAdmin(admin.ModelAdmin):
    list_display = ['id', 'member', 'get_media_name', 'borrowing_date', 'due_date']

    # Méthode pour afficher le nom du média emprunté
    def get_media_name(self, obj):
        if obj.media:  # Vérifie si le champ media est défini
            return f"{obj.media.name} ({obj.content_type})"
        return "Aucun média associé"

    # Personnalisation de l'en-tête de la colonne dans l'admin
    get_media_name.short_description = 'borrowed media'


admin.site.register(Member, MemberAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Cd, CdAdmin)
admin.site.register(Board_game, BoardGameAdmin)
admin.site.register(Dvd, DvdAdmin)
admin.site.register(Borrowing, BorrowingAdmin)
