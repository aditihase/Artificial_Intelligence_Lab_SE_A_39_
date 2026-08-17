print("Enter marks obtained in five subjects (out of 100):")

S1=float(input("enter marksS1:"))
S2=float(input("enter marksS2:"))
S3=float(input("enter marksS3:"))
S4=float(input("enter marksS4:"))
S5=float(input("enter marksS5:"))
 
total= S1+S2+S3+S4+S5
percentage=(total/500)*100

print("total marks::",total)
print("percentage ::",percentage,"%")

if (percentage <40):
   grade="fail"
elif(percentage<65):
   grade="ClassII"
elif(percentage<75):
  grade="ClassI"
else:
  grade="Distinction"
  
print("grade::",grade)


