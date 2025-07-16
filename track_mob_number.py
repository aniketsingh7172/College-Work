import phonenumbers
from phonenumbers import geocoder,carrier

mob_no=''
mobile=phonenumbers.parse(mob_no,'CH')
vailid=phonenumbers.is_valid_number(mobile)
ser_provider=carrier.name_for_number(mobile,'en')
print(geocoder.description_for_number(mobile, 'en'),"\n",vailid,"\n",ser_provider)