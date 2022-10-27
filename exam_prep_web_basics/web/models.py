from django.core import validators, exceptions
from django.db import models


def validate_only_alphanumeric(value):
    for ch in value:
        if not ch.isalnum() and ch != '_':
            raise exceptions.ValidationError("Ensure this value contains only letters, numbers, and underscore.")


class Profile(models.Model):
    MIN_USERNAME_LENGTH = 2
    MAX_USERNAME_LENGTH = 15

    username = models.CharField(
        max_length=MAX_USERNAME_LENGTH,
        validators=(
            validators.MinLengthValidator(MIN_USERNAME_LENGTH),
            validate_only_alphanumeric,
        ),
        null=False,
        blank=False,
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.PositiveIntegerField(
        null=True,
        blank=True,
    )


class Album(models.Model):
    MAX_ALBUM_NAME_LENGTH = 30
    MAX_ARTIST_NAME_LENGTH = 30
    MAX_GENRE_NAME_LENGTH = 30

    POP_MUSIC = 'Pop Music'
    JAZZ_MUSIC = 'Jazz Music'
    RNB_MUSIC = 'R&B Music'
    ROCK_MUSIC = 'Rock Music'
    COUNTRY_MUSIC = 'Country Music'
    DANCE_MUSIC = 'Dance Music'
    HIP_HOP_MUSIC = 'Hip Hop Music'
    OTHER_MUSIC = 'Other Music'

    MUSICS = (
        (POP_MUSIC, POP_MUSIC),
        (JAZZ_MUSIC, JAZZ_MUSIC),
        (RNB_MUSIC, RNB_MUSIC),
        (ROCK_MUSIC, ROCK_MUSIC),
        (COUNTRY_MUSIC, COUNTRY_MUSIC),
        (DANCE_MUSIC, DANCE_MUSIC),
        (HIP_HOP_MUSIC, HIP_HOP_MUSIC),
        (OTHER_MUSIC, OTHER_MUSIC),
    )

    album_name = models.CharField(
        max_length=MAX_ALBUM_NAME_LENGTH,
        unique=True,
        null=False,
        blank=False,
    )

    artist = models.CharField(
        max_length=MAX_ARTIST_NAME_LENGTH,
        null=False,
        blank=False,
    )

    genre = models.CharField(
        max_length=MAX_GENRE_NAME_LENGTH,
        null=False,
        blank=False,
        choices=MUSICS,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    price = models.FloatField(
        null=False,
        blank=False,
        validators=(
            validators.MinValueValidator(0.0),
        ),
    )
