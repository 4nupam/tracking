import phonenumbers
from phonenumbers import geocoder, carrier

def track_location(phone_number):
    try:
        parsed_number = phonenumbers.parse(phone_number, "CH")
        print(geocoder.description_for_number(parsed_number, "en"))
    except phonenumbers.phonenumberutil.NumberParseException as e:
        print("Error:", e)

def track_company(phone_number):
    try:
       carrier_number = phonenumbers.parse(phone_number, "RO")
       print(carrier.name_for_number(carrier_number, "en"))
    except phonenumbers.phonenumberutil.NumberParseException as e:
        print("Error:", e)

def track_state(phone_number):
    try:
        parsed_number = phonenumbers.parse(phone_number, "CH")
        city = geocoder.description_for_valid_number(parsed_number, "en")
        print(city.split(', ')[-1])
         # Extracting state
    except phonenumbers.phonenumberutil.NumberParseException as e:
        print("Error:", e)

def main():
    phone_number = input("Enter the phone number with country code ")
    track_location(phone_number)
    track_company(phone_number)
    track_state(phone_number)

main()
