
print "Please enter a number"

num1 = raw_input()

# check the var type
print type(num1)

# casting to an int from a string
if int(num1) >10:
    print "greater than 10"
else:
    print "else running here.."