raw_name = "   aDEOLA oKAfor  "
raw_email = "  Ade.Okafor@GMAIL.com  "
raw_phone = " 0803-123-4567 "

name = raw_name.strip().title()
email = raw_email.strip().lower()
phone = raw_phone.strip().replace("-", "").replace(" ", "")

print("Cleaned Student Profile")
print("Name:", name)
print("Email:", email)
print("Phone:", phone)

print("Email valid (has @):", "@" in email)
print("Phone valid (11 digits):", len(phone) == 11)
