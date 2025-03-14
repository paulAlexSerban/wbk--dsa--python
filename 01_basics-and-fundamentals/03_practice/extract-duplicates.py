ssn_name_pairs = {
    "333-444-555":"Pam Beesly",
    "111-222-333":"Paul ValJean",
    "333-444-555":"Pam Beesly",
    "222-333-444":"John Append",
    "333-444-555":"Pam Beesly"
}

def find_duplicate_names(ssn_name_dictionary: dict) -> dict:
  result = {}
  names = list(ssn_name_dictionary.values())

  for (ssn, name) in ssn_name_dictionary.items():
    if names.count(name) > 1:
      result[name] = result.get(name, [])
      result[name].append(ssn)
  return result

duplicate_name_ssn = find_duplicate_names(ssn_name_pairs)

for (name, ssn) in duplicate_name_ssn.items():
  print(f"Found duplicate name {name} with SSNs: {ssn}")