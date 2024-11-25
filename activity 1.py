medical_cause=input("did you have a medical cuase Y or N")
ATTEN= int(input("enter the attendance of the student"))
if medical_cause == "Y" :
    print("you are allowed")
else:
    if ATTEN>=75:
      print("allowed")
    else:
        print ("not allowed")