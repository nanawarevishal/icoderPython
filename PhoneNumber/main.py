

import phonenumbers
from test import number
from phonenumbers import geocoder
from phonenumbers import carrier

num = phonenumbers.parse(number,'CH')
print(geocoder.description_for_number(num,"en"))

serviceNumber = phonenumbers.parse(number,"RO")
print(carrier.name_for_number(serviceNumber,"en"))