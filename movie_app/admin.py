from django.contrib import admin
from .models import Movie
from django.db.models import QuerySet

# Register your models here.
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'rating', 'currency', 'budget', 'rating_status']
    list_editable = ['rating', 'currency', 'budget']
    # ordering = ['-rating', 'name']
    list_per_page = 10

    @admin.display(ordering='rating', description='Статус')
    def rating_status(self, mov:Movie) -> str:
        if mov.rating < 50:
            return 'Зачем это смотреть'
        if mov.rating < 70:
            return 'Разок можно глянуть'
        if mov.rating < 85:
            return 'Зачёт'
        return 'Топчик'

    def set_dollars(self, request, qs:QuerySet):
        qs.update(currency=Movie.USD)