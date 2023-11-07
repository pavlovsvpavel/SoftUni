import sys
from datetime import timedelta

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

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 20

        super().__init__(*args, **kwargs)

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
    card_number = MaskedCreditCardField()


class Hotel(models.Model):
    name = models.CharField(
        max_length=100
    )
    address = models.CharField(
        max_length=200
    )


class Room(models.Model):
    hotel = models.ForeignKey(
        to='Hotel',
        on_delete=models.CASCADE
    )
    number = models.CharField(max_length=100, unique=True)
    capacity = models.PositiveIntegerField()
    total_guests = models.PositiveIntegerField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        if self.total_guests > self.capacity:
            raise ValidationError('Total guests are more than the capacity of the room')

        super(Room, self).save(*args, **kwargs)

        return f'Room {self.number} created successfully'


class BaseReservation(models.Model):
    room = models.ForeignKey(
        to='Room',
        on_delete=models.CASCADE
    )
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        abstract = True

    def reservation_period(self):
        period_in_days = self.end_date.day - self.start_date.day

        return period_in_days

    def calculate_total_cost(self):
        total_cost = self.room.price_per_night * self.reservation_period()

        return round(total_cost, 1)


def check_for_existing_reservation(current_room: Room, res_type: str, start_date, end_date):
    reservation_type = getattr(sys.modules[__name__], res_type)
    res_room = reservation_type.objects.filter(
        room__number=current_room.number,
        start_date__lte=end_date,
        end_date__gte=start_date
    )

    return res_room


class RegularReservation(BaseReservation):
    def save(self, *args, **kwargs):
        if self.start_date >= self.end_date:
            raise ValidationError('Start date cannot be after or in the same end date')

        if check_for_existing_reservation(
                self.room,
                __class__.__name__,
                self.start_date,
                self.end_date):

            raise ValidationError(f"Room {self.room.number} cannot be reserved")

        super(RegularReservation, self).save(*args, **kwargs)

        return f"Regular reservation for room {self.room.number}"


class SpecialReservation(BaseReservation):
    def save(self, *args, **kwargs):
        if self.start_date >= self.end_date:
            raise ValidationError('Start date cannot be after or in the same end date')

        if check_for_existing_reservation(
                self.room,
                __class__.__name__,
                self.start_date,
                self.end_date):

            raise ValidationError(f"Room {self.room.number} cannot be reserved")

        super(SpecialReservation, self).save(*args, **kwargs)

        return f"Special reservation for room {self.room.number}"

    def extend_reservation(self, days: int):
        new_end_date = self.end_date + timedelta(days)

        if check_for_existing_reservation(
                self.room,
                __class__.__name__,
                self.start_date,
                self.end_date):

            raise ValidationError("Error during extending reservation")

        self.end_date = new_end_date
        self.save()

        return f"Extended reservation for room {self.room.number} with {days} days"
