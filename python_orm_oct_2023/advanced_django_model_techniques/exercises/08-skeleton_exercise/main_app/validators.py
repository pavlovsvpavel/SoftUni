from django.core.exceptions import ValidationError


def check_phone_number(value):
    if not value.startswith('+359') or len(value) != 13:
        raise ValidationError("Phone number must start with a '+359' followed by 9 digits")


# def check_name(value):
#     regex = '^[a-zA-Z ]+$'
#
#     if not re.search(regex, value):
#         raise ValidationError('Name can only contain letters and spaces')
