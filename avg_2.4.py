m1=int(input("enter a marks m1:"))
m2=int(input("enter a marks m2:"))
m2=int(input("enter a marks m3:"))
per=(m1+m2+m2)/3
if(per>=90):
    print("Excellent performance")
elif(per>=80):
    print("Very good performance")
elif(per>=70):
    print("Good performance")
elif(per>=60):
    print("Average performance")
else:
    print("Poor performance")