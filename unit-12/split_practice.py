countries = "Nigeria,Ghana,Kenya,Egypt,South Africa"
date = "27/11/2026"

country_list = countries.split(",")
date_parts = date.split("/")

print("Countries:", country_list)
print("Date parts:", date_parts)

print("First country:", country_list[0])
print("Last country:", country_list[4])

print("Day:", date_parts[0])
print("Month:", date_parts[1])
print("Year:", date_parts[2])
