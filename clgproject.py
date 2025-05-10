import json 
from textblob import TextBlob



# Step 1 :- Load the Json file
with open("mydata.json", "r") as file:
  teacherData = json.load(file)

#Step 2:- A function to check whether the user Input
def search_teacher_data(teacherData, userInput):
  userInput = userInput.lower()

  for teacher in teacherData:
  # Checking for age and city
    name = str(teacher.get("name", '')).lower()
    city = str(teacher.get('city', '')).lower()
    dept = str(teacher.get('department','')).lower()
    sec = str(teacher.get('sector', '')).lower()

    if userInput in name or userInput in city or userInput in dept or userInput in sec:
      print(f"YES! A teacher matched with {userInput}")
      return teacher


  print("Not found")
  return None

print("Search by Name, City, Department")
userInput = input()


# Calling the Function to get the matched teacher
found_teacher = search_teacher_data(teacherData,userInput)
print()


# Step 3:- Giving user the information
if found_teacher:
  print("What information do you want ?")
  while True:
   userInput2 = input("Phone, Email, Name, Department, City, Sector \n").lower()

   if userInput2 in found_teacher:
    print(f"{userInput2.capitalize()} : {found_teacher[userInput2]} \n")
    
    print("-------- exit to exit --------")
   if userInput2 == "exit":
     print("Exiting... ")  
     break
   
   print()
  else:
     print("The information is not available") 

else:
  print("No teacher match your input")    











# So we don't need to use found or not found 
# We don't need to brake because return do it for ourselves
# and if we return teacher it return the whole thing






  
