import re

# RegEx Validations Lab - Implementation
# This module contains regular expressions for validating names, phone numbers, and email addresses

# NOTE: There are only a few tests included, so multiple solutions will work.
# Feel free to encourage students to find oversights and add tests to this lab!

# Matches names starting with capital letter, allowing apostrophes and hyphens
# Examples: "John Cena", "Anya Taylor-Joy", "D'Angelo"
name = r"[A-Z][a-z]*'?[A-Za-z]*([- ][A-Z][a-z]*'?[A-Za-z]*)*"
name_regex = re.compile(name)

# Matches phone numbers in three formats:
# Examples: "5555555555", "555-555-5555", "(555) 555-5555"
phone_number = r"(\d{10}|\d{3}-\d{3}-\d{4}|\(\d{3}\) \d{3}-\d{4})"
phone_regex = re.compile(phone_number)

# Matches email addresses starting with letter, allowing dots and numbers, with @ and domain
email_address = r"[a-zA-Z][a-zA-Z0-9.]*@[a-zA-Z0-9]+\.[a-zA-Z]+"
email_regex = re.compile(email_address)
