import re

# NOTE: There are only a few tests included, so multiple solutions will work.
# Feel free to encourage students to find oversights and add tests to this lab!

# Matches names starting with capital letter, allowing apostrophes and hyphens
name = r"[A-Z][a-z]*'?[A-Za-z]*([- ][A-Z][a-z]*'?[A-Za-z]*)*"
name_regex = re.compile(name)

# Matches phone numbers in formats: 5555555555, 555-555-5555, (555) 555-5555
phone_number = r"(\d{10}|\d{3}-\d{3}-\d{4}|\(\d{3}\) \d{3}-\d{4})"
phone_regex = re.compile(phone_number)

email_address = r"[a-zA-Z][a-zA-Z0-9.]*@[a-zA-Z0-9]+\.[a-zA-Z]+"
email_regex = re.compile(email_address)
