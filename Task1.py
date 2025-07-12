#ask user for input and check its type
user_input = input("Enter any value: ")
print("The data type of your input is:", type(user_input))

#execute a string as Python code
code = input("Enter Python code to run: ")
try:
    result = eval(code)
    print("Result:", result)
except:
    exec(code)
