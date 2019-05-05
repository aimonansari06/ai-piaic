print("******MARKSHEET ASSIGNMENT******")
comp=int(input("Enter Your marks in Computer: "))
chem=int(input("Enter Your marks in Chemistry: "))
pst=int(input("Enter Your marks in Pakistan Studies: "))
sdh=int(input("Enter Your marks in Sindhi: "))
eng=int(input("Enter Your marks in English: "))
sum=comp+chem+pst+sdh+eng
Percentage=(sum*100)/425
if Percentage>=80 :
    print("Congratulations You Got Grade A-one\nPercentage ",Percentage)
elif Percentage<80 and Percentage>=70 :
    print("Congratulations You Got Grade A\nPercentage ",Percentage)
elif Percentage<70 and Percentage>=60 :
    print("You Got Grade B\nPercentage ",Percentage)
elif Percentage<60 and Percentage>=50 :
    print("You Got Grade C\nPercentage ",Percentage)
elif Percentage<50 and Percentage>=40 :
    print("You Got Grade D\nPercentage ",Percentage)
elif Percentage<40 and Percentage>=30:
    print("Failed\nYour Percentage ",Percentage)
else:
     print("Best of Luck")

    



