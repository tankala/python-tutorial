# from units import weight_converter, distance_converter

# print(weight_converter.kgs_to_pounds_number)
# print(distance_converter.kms_to_miles(10))

from units import weight_converter as wc
from units.distance_converter import miles_to_kms

print(wc.kgs_to_pounds_number)
print(miles_to_kms(100))