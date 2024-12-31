from django.db import models
from django.utils.safestring import mark_safe


class country(models.Model):
    id = models.IntegerField(primary_key=True)
    country_name=models.CharField(max_length=50)

    def __str__(self):
        return self.country_name
class state(models.Model):
    id = models.IntegerField(primary_key=True)
    country_id=models.ForeignKey(country, on_delete=models.CASCADE)
    state_name=models.CharField(max_length=50)
    def __str__(self):
        return self.state_name
class city(models.Model):
    id = models.IntegerField(primary_key=True)
    state_id=models.ForeignKey(state, on_delete=models.CASCADE)
    city_name=models.CharField(max_length=50)
    def __str__(self):
        return self.city_name
class actor(models.Model):
    id = models.IntegerField(primary_key=True)
    a_state=models.ForeignKey(state, on_delete=models.CASCADE)
    a_country=models.ForeignKey(country, on_delete=models.CASCADE)
    a_city=models.ForeignKey(city, on_delete=models.CASCADE)
    a_name=models.CharField(max_length=50)
    a_pic=models.ImageField(upload_to='photos/')
    a_bio=models.TextField()
    a_nationality=models.CharField(max_length=50)
    a_awards=models.TextField()
    a_gender=models.CharField(max_length=50)
    a_birthdate=models.DateField()

    def display_image(self, obj):
        return format_html('<img src="{}" style="width: 100px; height: auto;" />', obj.image.url)

    display_image.short_description = 'Image Preview'

class user(models.Model):
    id = models.IntegerField(primary_key=True)
    u_state=models.ForeignKey(state, on_delete=models.CASCADE)
    u_country=models.ForeignKey(country, on_delete=models.CASCADE)
    u_city=models.ForeignKey(city, on_delete=models.CASCADE)
    u_name=models.CharField(max_length=50)
    u_dp=models.ImageField(upload_to='photos/')
    u_gender=models.CharField(max_length=50)
    u_gmail=models.EmailField()
    u_phone=models.CharField(max_length=50)
    u_status=models.BooleanField()
    u_date_joined=models.DateField()
    def __str__(self):
        return self.u_name
class director(models.Model):
    id = models.IntegerField(primary_key=True)
    d_state=models.ForeignKey(state, on_delete=models.CASCADE)
    d_country=models.ForeignKey(country, on_delete=models.CASCADE)
    d_city=models.ForeignKey(city, on_delete=models.CASCADE)
    d_name=models.CharField(max_length=50)
    d_pic=models.ImageField(upload_to='photos/')
    d_bio=models.TextField()
    d_nationality=models.CharField(max_length=50)
    d_awards=models.TextField()
    d_gender=models.CharField(max_length=50)

    def __str__(self):
        return self.d_name
class genre(models.Model):
    name=models.CharField(max_length=100)

class movie(models.Model):
    id = models.IntegerField(primary_key=True)
    title=models.CharField(max_length=50)
    description=models.TextField()
    release_year=models.CharField(max_length=50)
    genre=models.ForeignKey(genre, on_delete=models.CASCADE)
    actor=models.ForeignKey(actor, on_delete=models.CASCADE)
    director=models.ForeignKey(director, on_delete=models.CASCADE)
    poster=models.ImageField(upload_to='photos/')
    trailer=models.URLField()
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.genre
class reviews(models.Model):
    movie=models.ForeignKey(movie, on_delete=models.CASCADE)
    user=models.ForeignKey(user, on_delete=models.CASCADE)
    rating=models.IntegerField()
    comments=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.rating
class watchlist(models.Model):
     user=models.ForeignKey(user, on_delete=models.CASCADE)
     movie=models.ForeignKey(movie, on_delete=models.CASCADE)
     added_at=models.DateTimeField(auto_now_add=True)





