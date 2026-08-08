passwords = input("Enter password:")
while True:

   if len(passwords) >= 8:
    pass
   elif any(char.issuper() for char in passwords):
    pass
   elif any(char.islower() for char in passwords):
    pass
   elif any(char.isdigit() for char in passwords): 
    pass
