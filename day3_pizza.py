print("welcome to pyhton pizza deliveries")
size=input("what size do u want ? s, m or l\n")
if size=="s":
    bill= 15
    pep=input("do u want peperoni? y or n\n" )
    if pep=="y":
        bill+=2
    else:
        bill=bill
elif size=="m":
    bill= 20
    pep=input("do u want peperoni? y or n\n" )
    if pep=="y":
        bill+=3
    else:
        bill=bill
else :
    bill=25
    pep=input("do u want peperoni? y or n\n" )
    if pep=="y":
        bill+=3
    else:
        bill=bill
cheese=input("do u want extra cheese ? y or n\n")
if cheese=='y':
    bill+=1
else :
    bill=bill
print(f"ur total bill is {bill}")