#Runs in the terminal perfectly         

hrs = input("Enter Hours:")
rate = input("Enter Rate:")

try: # if it fails because user entered a word - except would run
   nh = float(hrs) #number of hours
   hr = float(rate) #hour rate

except:
   print('Enter a number, not a word')
   quit()

bill = nh * hr

if nh <= 40:
   print(bill)
elif nh > 40:
   sr = 40 * hr #standard payment
   ohr = hr * 1.5 #overtime hours rate
   pay = sr+(ohr*(nh-40))
   print(pay)
