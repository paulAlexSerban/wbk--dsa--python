# store key-value pairs
# a key identifies a specific item
# each key must be unique

old_dictionary = dict()
new_short_dictionary = {}

ssn_name_pairs = {}
ssn_name_pairs["123-321-111"] = "John Append"
ssn_name_pairs["123-321-333"] = "Alter John"
ssn_name_pairs = {
  "123-321-444": "Le Paul John",
  "000-000-999": "John Append"
  }
key = "000-000-99s"
if key in ssn_name_pairs:
  del ssn_name_pairs[key]
else:
  print(f"Invalid Key {key}")

