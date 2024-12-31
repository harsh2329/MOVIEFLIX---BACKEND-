from django.contrib import admin
from .models import *


@admin.register(country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'country_name')

@admin.register(state)
class StateAdmin(admin.ModelAdmin):
    list_display = ('id', 'country_id', 'state_name')
    list_editable = ('state_name',)

@admin.register(city)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'state_id', 'city_name')
    list_filter = ('state_id', 'city_name')

@admin.register(actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('id', 'a_state', 'a_country', 'a_city', 'a_name', 'display_image', 'a_nationality', 'a_bio',  'a_gender', 'a_birthdate')



@admin.register(user)
class userAdmin(admin.ModelAdmin):
    list_display = ('id', 'u_state', 'u_country', 'u_city', 'u_name', 'u_dp', 'u_gender', 'u_gmail', 'u_gmail', 'u_phone', 'u_status', 'u_date_joined')

@admin.register(director)
class directorAdmin(admin.ModelAdmin):
    list_display = ('id', 'd_state', 'd_country', 'd_city', 'd_name', 'd_pic', 'd_bio', 'd_nationality', 'd_awards', 'd_gender')

@admin.register(genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'release_year', 'genre', 'actor', 'director', 'poster', 'trailer', 'created_at')

@admin.register(reviews)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('movie', 'user', 'rating', 'comments', 'created_at')

@admin.register(watchlist)
class WatchlistAdmin(admin.ModelAdmin):
    list_display = ('user', 'movie', 'added_at')

