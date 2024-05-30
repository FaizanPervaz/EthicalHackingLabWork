import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

phone_number1 = phonenumbers.parse("+923000000000")
carrier1 = phonenumbers.parse("+923000000000")

print(geocoder.description_for_number(phone_number1, "en"))
print(carrier.name_for_number(carrier1, "en"))

