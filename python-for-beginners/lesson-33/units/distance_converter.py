miles_to_kms_number = 1.6

def miles_to_kms(distance_in_miles):
    distance_in_miles = float(distance_in_miles)
    distance_in_kms = distance_in_miles * miles_to_kms_number
    return distance_in_kms

def kms_to_miles(distance_in_kms):
    distance_in_kms = float(distance_in_kms)
    distance_in_miles = distance_in_kms / miles_to_kms_number
    return distance_in_miles
