messy_name = "   dSgBoY   "
messy_state = "  oSUN   nIGERIA  "

print(f"Original name: [{messy_name}]")
print(f"Original state: [{messy_state}]")

clean_name = messy_name.strip().title()
clean_state = messy_state.strip().title().replace("   ", " ")

print(f"Cleaned name: [{clean_name}]")
print(f"Cleaned state: [{clean_state}]")
