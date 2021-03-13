# from units import weight_converter as wc, distance_converter as dc

# print(wc.kgs_to_pounds_number)
# print(dc.kms_to_miles(5))

from units import weight_converter as wc
from units.distance_converter import miles_to_kms

print(wc.kgs_to_pounds_number)
print(miles_to_kms(10))