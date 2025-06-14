# comapny email generating
import sys


full_name = " ".join(sys.argv[1:])


email = full_name.lower().replace(" ",".") + "@company.com"

print("\n --- Your profile ---")
print("Full Name:", full_name)
print("Generated Email:", email)
