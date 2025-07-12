#get maths expression from user
expression = input("Enter a Python expression (2 + 3 * 4): ")

#safely evaluate it using exec and print the result
code = f"result = {expression}"
exec(code)
print("The result of your expression is:", locals()['result'])
