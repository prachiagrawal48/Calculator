#-----Simple Calculator Using Python Program
#Function to add two numbers
def add(num1,num2):
    return num1+num2

#Function to subtract two numbers
def subtract(num1,num2):
    return num1-num2

#Function to multiply two numbers
def multiply(num1,num2):
    return num1*num2

#Function to divide two numbers
def divide(num1,num2):
    if num2==0:
        return "Error:Division by zero is not allowed."
    return num1/num2

#Main calculator logic
result = None
def calculator():
   print("Simple Calculator")
   print("Select the operation")
   print("1.Add(+)")
   print("2.Subtract(-)")
   print("3.Multiply(*)")
   print("4.Divide(/)")

while True:
    #Take input from the user for the operation choice
    choice = input("Enter choice (1/2/3/4):")

#check if choice is one of the four options
    if choice in("1","2","3","4"):


        try:
            #Prompt the user for the two numbers
            num1= float(input("Enter the first number:"))
            num2= float(input("Enter the second number:"))
        except ValueError:
            print("Invalid input.Please enter a valid number.")
            continue
        #Perform the calculation based on the choice
        operation_symbol= None
        if choice=="1":
            result = add(num1,num2)
            operation_symbol='+'
        elif choice =="2":
            result = subtract(num1,num2)
            operation_symbol='-'
        elif choice =="3":
            result = multiply(num1,num2)
            operation_symbol='*'           
        elif choice =="4":   
            result = divide(num1,num2)
            operation_symbol='/'
        #Display the result

        if isinstance(result,str):

        #Handles the division by zero error message
          print(result)
        else:
        #Display the successful calculation
          print(f"\nResult:{num1}{operation_symbol}{num2}={result}")
        #Display the successful calculation
        next_calculation = input("\nDo you want to perform another calculation?(yes/no):")
        if next_calculation.lower() == 'no':
              print("Calculator closed.Goodbye!")

              break
        else:
              print("Invalid Input.Please enter a choice between 1 and 4.")

        #Run the calculator function
        calculator()                      