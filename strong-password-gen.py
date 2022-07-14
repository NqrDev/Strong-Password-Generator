import string
import random

s1 = list(string.ascii_lowercase) #abcdefghijklmnopqrstuvwxyz
s2 = list(string.ascii_uppercase) #ABCDEFGHIJKLMNOPQRSTUVWXYZ
s3 = list(string.digits) #123456789
s4 = list(string.punctuation) #,.
cn = input("How Many Caracters Of Input : ")

while True:
    try:
        cn = int(cn)
        if cn < 6 :
            print("Pls Input At Least 6 Caracters..!!")
            cn = input("Pls Enter Number Carachter Again : ")
        else:
            break
    except:
        print("Pls Enter Number Onlyy :!")
        cn = input("Pls Enter Number Carachter Again : ")

random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

p1 = round(cn*(30/100))
p2 = round(cn*(20/100))

p = []

for i in range(p1):
    p.append(s1[i])
    p.append(s2[i])

for i in range(p2):
    p.append(s3[i])
    p.append(s4[i])

random.shuffle(p)

p = "".join(p[0:])

print("This Is The Strong Password Please Save it")
print(p)
