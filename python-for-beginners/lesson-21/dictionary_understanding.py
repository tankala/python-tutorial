registration_state_dictionary = {
    "AP": "Andhra Pradesh",
    "TS": "Telangana"
}

sub_dictionary = {
    "GJ": "Gujarat",
    "OD": "Odistha"
}

registration_state_dictionary.update(sub_dictionary)
print(registration_state_dictionary)

# Dictionary items list
# print(registration_state_dictionary.items())

# Dictionary values list
# print(registration_state_dictionary.values())

# Dictionary keys list
# print(registration_state_dictionary.keys())

# Clearing the dictionary
# registration_state_dictionary.clear()
# print(registration_state_dictionary)

# Value Updation
# registration_state_dictionary["AP"] = "Andhra State"

# if "dl" in registration_state_dictionary
# print(registration_state_dictionary["AP"])

# print(registration_state_dictionary.get("dl", "Invalid State"))

# Insert or add
# registration_state_dictionary["DL"] = "New Delhi"
# print(registration_state_dictionary)