kgs_to_pounds_number = 2.205

def kgs_to_pounds(weight_in_kgs):
    weight_in_kgs = float(weight_in_kgs)
    weight_in_pounds = weight_in_kgs * kgs_to_pounds_number
    return weight_in_pounds

def pounds_to_kgs(weight_in_pounds):
    weight_in_pounds = float(weight_in_pounds)
    weight_in_kgs = weight_in_pounds / kgs_to_pounds_number
    return weight_in_kgs