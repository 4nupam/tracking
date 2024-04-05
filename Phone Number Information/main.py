import phonenumbers
from phonenumbers import geocoder,carrier

def track_country(phone_number):
    try:
       prased_number = phonenumbers.parse(phone_number,"CH")
       print(geocoder.description_for_number(prased_number,"en")) 
    except phonenumbers.phonenumberutil.NumberParseException as e:
       print("Error ",e)

def track_company(phone_number):
    try:
      prased_number = phonenumbers.parse(phone_number,"CH")
      print(carrier.name_for_number(prased_number,"en"))

    except phonenumbers.phonenumberutil.NumberParseException as e:
       print("Error",e)

def main():
   phone_number = input("Enter the number ")
   track_country(phone_number)
   track_company(phone_number)

main()
