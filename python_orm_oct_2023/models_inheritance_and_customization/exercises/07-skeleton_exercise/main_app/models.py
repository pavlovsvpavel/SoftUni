from django.core import validators
from django.core.exceptions import ValidationError
from django.db import models


class BaseCharacter(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        abstract = True


class Mage(BaseCharacter):
    elemental_power = models.CharField(max_length=100)
    spellbook_type = models.CharField(max_length=100)


class Assassin(BaseCharacter):
    weapon_type = models.CharField(max_length=100)
    assassination_technique = models.CharField(max_length=100)


class DemonHunter(BaseCharacter):
    weapon_type = models.CharField(max_length=100)
    demon_slaying_ability = models.CharField(max_length=100)


class TimeMage(Mage):
    time_magic_mastery = models.CharField(max_length=100)
    temporal_shift_ability = models.CharField(max_length=100)


class Necromancer(Mage):
    raise_dead_ability = models.CharField(max_length=100)


class ViperAssassin(Assassin):
    venomous_strikes_mastery = models.CharField(max_length=100)
    venomous_bite_ability = models.CharField(max_length=100)


class ShadowbladeAssassin(Assassin):
    shadowstep_ability = models.CharField(max_length=100)


class VengeanceDemonHunter(DemonHunter):
    vengeance_mastery = models.CharField(max_length=100)
    retribution_ability = models.CharField(max_length=100)


class FelbladeDemonHunter(DemonHunter):
    felblade_ability = models.CharField(max_length=100)


class UserProfile(models.Model):
    username = models.CharField(
        max_length=70,
        unique=True,
    )
    email = models.EmailField(unique=True)
    bio = models.TextField(
        blank=True,
        null=True
    )


class Message(models.Model):
    sender = models.ForeignKey(
        to='UserProfile',
        on_delete=models.CASCADE,
        related_name='sent_messages'
    )
    receiver = models.ForeignKey(
        to='UserProfile',
        on_delete=models.CASCADE,
        related_name='received_messages'
    )
    content = models.TextField()
    timestamp = models.DateTimeField(
        auto_now_add=True,
    )
    is_read = models.BooleanField(default=False)

    def mark_as_read(self):
        self.is_read = True
        self.save()

    def mark_as_unread(self):
        self.is_read = False
        self.save()

    def reply_to_message(self, reply_content, receiver):
        message = Message.objects.create(
            sender=self.receiver,
            receiver=receiver,
            content=reply_content
        )

        self.mark_as_read()

        return message

    def forward_message(self, sender, receiver):
        message = Message.objects.create(
            sender=sender,
            receiver=receiver,
            content=self.content
        )

        return message


class StudentIDField(models.PositiveIntegerField):
    def to_python(self, value):
        if isinstance(value, int):
            return value


class Student(models.Model):
    name = models.CharField(max_length=100)
    student_id = StudentIDField()


class MaskedCreditCardField(models.CharField):
    MAX_LENGTH_CARD_NUMBER = 16

    def to_python(self, value):
        if not isinstance(value, str):
            raise ValidationError('The card number must be a string')

        if not value.isdigit():
            raise ValidationError('The card number must contain only digits')

        if len(value) != self.MAX_LENGTH_CARD_NUMBER:
            raise ValidationError('The card number must be exactly 16 characters long')

        last_four_card_digits = value[-4:]

        return f"****-****-****-{last_four_card_digits}"


class CreditCard(models.Model):
    card_owner = models.CharField(max_length=100)
    card_number = MaskedCreditCardField(max_length=20)


class Hotel(models.Model):
    name = models.CharField(max_length=100),
    address = models.CharField(max_length=200),


def to_python(value):
    return int(value)


class Room(models.Model):

    number = models.CharField(max_length=100, unique=True)
    capacity = int(models.PositiveIntegerField())
    total_guests = models.PositiveIntegerField(
        validators=[validators.MaxValueValidator(
            capacity, message='Total guests are more than the capacity of the room')]
    )
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return f'Room {self.number} created successfully'
