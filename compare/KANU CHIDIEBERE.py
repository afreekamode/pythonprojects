# Python Program - WAEC RESULT COMPILER
subject = int(input("\nENTER TOTAL NUMBER OF SUBJECTS OFFERED: "));
if subject !=9:  
   print("CHECK YOUR INPUT")
#elif subject = int(input("ENTER TOTAL NUMBER OF SUBJECTS OFFERED: ")):
   	
else:
   mark1 = int(input("ENTER ENGLISH SCORE: "));    
   mark2 = int(input("ENTER MATHEMATICS SCORE: "));     
   mark3 = int(input("ENTER PHYSIC SCORE: "));     
   mark4 = int(input("ENTER BIOLOGY SCORE: " ));     
   mark5 = int(input("ENTER CHEMISTRY SCORE: "));
   mark6 = int(input("ENTER AGRIC SCI. SCORE: ")); 
   mark7 = int(input("ENTER ECONOMICS SCORE: " ));     
   mark8 = int(input("ENTER GOVERNMENT SCORE: " ));     
   mark9 = int(input("ENTER C.R.K SCORE: " ));     

# ENGLISH GRADE  
print("\n\nTHIS IS THE WAEC RESULT")
print("\nSUBJECTS\tGRADE\tREMARK")
if(mark1>=80 and mark1<=100):
   print("ENGLISH \tA1 \tEXCELLENT"); 
elif(mark1>=70 and mark1<=79): 
   print("ENGLISH \tB2 \tVERY GOOD");
elif(mark1>=65 and mark1<=69): 
   print("ENGLISH \tB3 \tGOOD");
elif(mark1>=60 and mark1<=64): 
   print("ENGLISH \tC4 \tCREDIT");
elif(mark1>=55 and mark1<=59): 
   print("ENGLISH \tC5 \tCREDIT");
elif(mark1>=50 and mark1<=54): 
   print("ENGLISH \tC6 \tCREDIT");
elif(mark1>=45 and mark1<=49): 
   print("ENGLISH \tD7 \tPASS");
elif(mark1>=40 and mark1<=44): 
   print("ENGLISH \tE8 \tPASS");
else:#(mark1>=0 and mark<=39): 
   print("ENGLISH \tF9 \tFAIL");

#MATHEMATICS GRADE
if(mark2>=80 and mark2<=100):
   print("MATHEMATICS \tA1 \tEXCELLENT"); 
elif(mark2>=70 and mark2<=79): 
   print("MATHEMATICS \tB2 \tVERY GOOD");
elif(mark2>=65 and mark2<=69): 
   print("MATHEMATICS \tB3 \tGOOD");
elif(mark2>=60 and mark2<=64): 
   print("MATHEMATICS \tC4 \tCREDIT");
elif(mark2>=55 and mark2<=59): 
   print("MATHEMATICS \tC5 \tCREDIT");
elif(mark2>=50 and mark2<=54): 
   print("MATHEMATICS \tC6 \tCREDIT");
elif(mark2>=45 and mark2<=49): 
   print("MATHEMATICS \tD7 \tPASS");
elif(mark2>=40 and mark2<=44): 
   print("MATHEMATICS \tE8 \tPASS");
else: 
   print("MATHEMATICS \tF9 \tFAIL");  
   
#PHYSICS GRADE
if(mark3>=80 and mark3<=100):
   print("PHYSICS \tA1 \tEXCELLENT"); 
elif(mark3>=70 and mark3<=79): 
   print("PHYSICS \tB2 \tVERY GOOD");
elif(mark3>=65 and mark3<=69): 
   print("PHYSICS \tB3 \tGOOD");
elif(mark3>=60 and mark3<=64): 
   print("PHYSICS \tC4 \tCREDIT");
elif(mark3>=55 and mark3<=59): 
   print("PHYSICS \tC5 \tCREDIT");
elif(mark3>=50 and mark3<=54): 
   print("PHYSICS \tC6 \tCREDIT");
elif(mark3>=45 and mark3<=49): 
   print("PHYSICS \tD7 \tPASS");
elif(mark3>=40 and mark3<=44): 
   print("PHYSICS \tE8 \tPASS");
else: 
   print("PHYSICS \tF9 \tFAIL");

#BIOLOGY GRADE
if(mark4>=80 and mark4<=100):
   print("BIOLOGY \tA1 \tEXCELLENT"); 
elif(mark4>=70 and mark4<=79): 
   print("BIOLOGY \tB2 \tVERY GOOD");
elif(mark4>=65 and mark4<=69): 
   print("BIOLOGY \tB3 \tGOOD");
elif(mark4>=60 and mark4<=64): 
   print("BIOLOGY \tC4 \tCREDIT");
elif(mark4>=55 and mark4<=59): 
   print("BIOLOGY \tC5 \tCREDIT");
elif(mark4>=50 and mark4<=54): 
   print("BIOLOGY \tC6 \tCREDIT");
elif(mark4>=45 and mark4<=49): 
   print("BIOLOGY \tD7 \tPASS");
elif(mark4>=40 and mark4<=44): 
   print("BIOLOGY \tE8 \tPASS");
else:
   print("BIOLOGY \tF9 \tFAIL");
   
#CHEMISTRY GRADE
if(mark5>=80 and mark5<=100):
   print("CHEMISTRY \tA1 \tEXCELLENT"); 
elif(mark5>=70 and mark5<=79): 
   print("CHEMISTRY \tB2 \tVERY GOOD");
elif(mark5>=65 and mark5<=69): 
   print("CHEMISTRY \tB3 \tGOOD");
elif(mark5>=60 and mark5<=64): 
   print("CHEMISTRY \tC4 \tCREDIT");
elif(mark5>=55 and mark5<=59): 
   print("CHEMISTRY \tC5 \tCREDIT");
elif(mark5>=50 and mark5<=54): 
   print("CHEMISTRY \tC6 \tCREDIT");
elif(mark5>=45 and mark5<=49): 
   print("CHEMISTRY \tD7 \tPASS");
elif(mark5>=40 and mark5<=44): 
   print("CHEMISTRY \tE8 \tPASS");
else: 
   print("CHEMISTRY \tF9 \tFAIL");

#AGRIC SCI. GRADE
if(mark6>=80 and mark6<=100):
   print("AGRIC SCI. \tA1 \tEXCELLENT"); 
elif(mark6>=70 and mark6<=79): 
   print("AGRIC SCI. \tB2 \tVERY GOOD");
elif(mark6>=65 and mark6<=69): 
   print("AGRIC SCI. \tB3 \tGOOD");
elif(mark6>=60 and mark6<=64): 
   print("AGRIC SCI. \tC4 \tCREDIT");
elif(mark6>=55 and mark6<=59): 
   print("AGRIC SCI. \tC5 \tCREDIT");
elif(mark6>=50 and mark6<=54): 
   print("AGRIC SCI. \tC6 \tCREDIT");
elif(mark6>=45 and mark6<=49): 
   print("AGRIC SCI. \tD7 \tPASS");
elif(mark6>=40 and mark6<=44): 
   print("AGRIC SCI. \tE8 \tPASS");
else: 
   print("AGRIC SCI. \tF9 \tFAIL");

#ECONOMICS GRADE
if(mark7>=80 and mark7<=100):
   print("ECONOMICS \tA1 \tEXCELLENT"); 
elif(mark7>=70 and mark7<=79): 
   print("ECONOMICS \tB2 \tVERY GOOD");
elif(mark7>=65 and mark7<=69): 
   print("ECONOMICS \tB3 \tGOOD");
elif(mark7>=60 and mark7<=64): 
   print("ECONOMICS \tC4 \tCREDIT");
elif(mark7>=55 and mark7<=59): 
   print("ECONOMICS \tC5 \tCREDIT");
elif(mark7>=50 and mark7<=54): 
   print("ECONOMICS \tC6 \tCREDIT");
elif(mark7>=45 and mark7<=49): 
   print("ECONOMICS \tD7 \tPASS");
elif(mark7>=40 and mark7<=44): 
   print("ECONOMICS \tE8 \tPASS");
else: 
   print("ECONOMICS \tF9 \tFAIL");

#GOVERNMENT GRADE 
if(mark8>=80 and mark8<=100):
   print("GOVERNMENT \tA1 \tEXCELLENT"); 
elif(mark8>=70 and mark8<=79): 
   print("GOVERNMENT \tB2 \tVERY GOOD");
elif(mark8>=65 and mark8<=69): 
   print("GOVERNMENT \tB3 \tGOOD");
elif(mark8>=60 and mark8<=64): 
   print("GOVERNMENT \tC4 \tCREDIT");
elif(mark8>=55 and mark8<=59): 
   print("GOVERNMENT \tC5 \tCREDIT");
elif(mark8>=50 and mark8<=54): 
   print("GOVERNMENT \tC6 \tCREDIT");
elif(mark8>=45 and mark8<=49): 
   print("GOVERNMENT \tD7 \tPASS");
elif(mark8>=40 and mark8<=44): 
   print("GOVERNMENT \tE8 \tPASS");
else: 
   print("GOVERNMENT \tF9 \tFAIL");

#C.R.K GRADE
if(mark9>=80 and mark9<=100):
   print("C.R.K \t\tA1 \tEXCELLENT"); 
elif(mark9>=70 and mark9<=79): 
   print("C.R.K \t\tB2 \tVERY GOOD");
elif(mark9>=65 and mark9<=69): 
   print("C.R.K \t\tB3 \tGOOD");
elif(mark9>=60 and mark9<=64): 
   print("C.R.K \t\tC4 \tCREDIT");
elif(mark9>=55 and mark9<=59): 
   print("C.R.K \t\tC5 \tCREDIT");
elif(mark9>=50 and mark9<=54): 
   print("C.R.K \t\tC6 \tCREDIT");
elif(mark9>=45 and mark9<=49): 
   print("C.R.K \t\tD7 \tPASS");
elif(mark9>=40 and mark9<=44): 
   print("C.R.K \t\tE8 \tPASS");
else: 
   print("C.R.K \t\tF9 \tFAIL");

sum = int(mark1+mark2+mark3+mark4+mark5+mark6+mark7+mark8+mark9)
ave = int(sum)/9
print("\nTHE TOTAL SCORE= ",sum)
print("THE AVERAGE SCORE= ", ave)

import time 
localtime = time.asctime( time.localtime(time.time()) ) 
print ("DATE AND TIME :", localtime)
'''import calendar 
cal = calendar.month(2018, 7) 
print ("Here is the calendar:") 
print (cal)'''

print("...CONGRATULATIONS...")