smallest = None
largest = None
while True:
    num = input('Enter a number: ')
    if num == 'done':
       break
    try:
       inum = int(num)
    except:
       print('Invalid input')
       continue
    if smallest is None:
       smallest = inum
    if smallest > inum:
       smallest = inum
    if largest is None:
       largest = inum
    if inum > largest:
       largest = inum

print('Maximum is', largest)
print('Minimum is', smallest)
