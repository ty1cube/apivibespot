# Generated by Django 2.1.5 on 2019-02-25 18:08

import dashboard.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authentications', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlbumList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, max_length=100, null=True)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=dashboard.models.upload_album_image)),
                ('year', models.CharField(blank=True, max_length=100, null=True)),
                ('track_count', models.IntegerField(blank=True, default=0, null=True)),
                ('release_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.BooleanField(blank=True, null=True, verbose_name=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'albums',
            },
        ),
        migrations.CreateModel(
            name='MusicPlayList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'music_playlists',
            },
        ),
        migrations.CreateModel(
            name='PlayListDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('playlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.MusicPlayList')),
            ],
            options={
                'db_table': 'music_playlists_details',
            },
        ),
        migrations.CreateModel(
            name='SongList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, max_length=100, null=True)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('label_name', models.CharField(blank=True, max_length=100, null=True)),
                ('genre', models.CharField(blank=True, max_length=50, null=True)),
                ('release_date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=dashboard.models.upload_song_image)),
                ('song', models.FileField(blank=True, null=True, upload_to=dashboard.models.upload_singles)),
                ('duration', models.CharField(blank=True, max_length=10, null=True)),
                ('stream', models.IntegerField(blank=True, default=0, null=True)),
                ('streamed', models.IntegerField(blank=True, default=0, null=True)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('featured_artist', models.CharField(blank=True, max_length=100, null=True)),
                ('contributors', models.CharField(blank=True, max_length=100, null=True)),
                ('recording_year', models.DateField(auto_now_add=True, null=True)),
                ('status', models.BooleanField(blank=True, null=True, verbose_name=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('album', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.AlbumList')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='authentications.Country')),
                ('push_city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='authentications.LocalArea')),
                ('push_state', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pushstate', to='authentications.State')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vibe_state', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vibestate', to='authentications.State')),
            ],
            options={
                'db_table': 'songs',
            },
        ),
        migrations.CreateModel(
            name='UserEarning',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('earned_currency', models.CharField(max_length=50)),
                ('earned_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('track', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.SongList')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_earning',
            },
        ),
        migrations.AddField(
            model_name='playlistdetail',
            name='track',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.SongList'),
        ),
        migrations.AddField(
            model_name='playlistdetail',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
