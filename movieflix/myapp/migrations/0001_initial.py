# Generated by Django 5.0.7 on 2024-07-11 04:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='city',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('city_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='country',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('country_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='actor',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('a_name', models.CharField(max_length=50)),
                ('a_pic', models.ImageField(upload_to='')),
                ('a_bio', models.TextField()),
                ('a_nationality', models.CharField(max_length=50)),
                ('a_awards', models.TextField()),
                ('a_gender', models.CharField(max_length=50)),
                ('a_birthdate', models.DateField()),
                ('a_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.city')),
                ('a_country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.country')),
            ],
        ),
        migrations.CreateModel(
            name='director',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('d_name', models.CharField(max_length=50)),
                ('d_pic', models.ImageField(upload_to='')),
                ('d_bio', models.TextField()),
                ('d_nationality', models.CharField(max_length=50)),
                ('d_awards', models.TextField()),
                ('d_gender', models.CharField(max_length=50)),
                ('d_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.city')),
                ('d_country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.country')),
            ],
        ),
        migrations.CreateModel(
            name='movie',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('release_year', models.CharField(max_length=50)),
                ('poster', models.ImageField(upload_to='')),
                ('trailer', models.URLField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.actor')),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.director')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.genre')),
            ],
        ),
        migrations.CreateModel(
            name='state',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('state_name', models.CharField(max_length=50)),
                ('country_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.country')),
            ],
        ),
        migrations.AddField(
            model_name='director',
            name='d_state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.state'),
        ),
        migrations.AddField(
            model_name='city',
            name='state_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.state'),
        ),
        migrations.AddField(
            model_name='actor',
            name='a_state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.state'),
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('u_name', models.CharField(max_length=50)),
                ('u_dp', models.ImageField(upload_to='')),
                ('u_gender', models.CharField(max_length=50)),
                ('u_gmail', models.EmailField(max_length=254)),
                ('u_phone', models.CharField(max_length=50)),
                ('u_status', models.BooleanField()),
                ('u_date_joined', models.DateField()),
                ('u_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.city')),
                ('u_country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.country')),
                ('u_state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.state')),
            ],
        ),
        migrations.CreateModel(
            name='reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('comments', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='watchlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_at', models.DateTimeField(auto_now_add=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
            ],
        ),
    ]
