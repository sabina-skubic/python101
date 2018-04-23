# x = int(raw_input("Enter the value for x: "))
# print x
#
# y = int(raw_input("Enter the value for y: "))
# print y
#
# print x + y
#
# x='3'
# y=5
# print x+y
# x = int(raw_input("Enter the value for x: "))
# y = int(raw_input("Enter the value for y: "))
# operation = raw_input("Choose math operation (+, -, *, /): ")
#
# if operation =='+':
#     print x+y
# elif operation=='-':
#     print x-y
# elif operation=='*':
#     print x*y
# else:
#     print x/y

x = int(raw_input("Enter the value for x: "))
y = int(raw_input("Enter the value for y: "))
operation = raw_input("Choose math operation (+, -, *, /): ")

if operation =='+':
    res_x_y= x + y
elif operation=='-':
    res_x_y= x - y
elif operation=='*':
    res_x_y= x * y
elif operation=='/':
    res_x_y= float(x) / float(y)
else:
    res_x_y='Invalid operation'
print res_x_y






