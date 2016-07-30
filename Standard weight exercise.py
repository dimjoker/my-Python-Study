# -*- coding: utf-8 -*-
# This is the Standard weight exercise
# python 2.x
# no while or for, just a simple exercise

def standard_weight():
    print "Please input your information:"
    gender = raw_input("Your gender(male female or other) > ")
    
    if gender == "male":
        height = float(raw_input("Your height > "))
        standard_weight = (height - 80) * 70 / 100
        tip = "Your standard weight is %d" % standard_weight
        return tip
            
    elif gender == "female":
        height = float(raw_input("Your height > "))
        standard_weight = (height - 70) * 60 / 100
        tip = "Your standard weight is %d" % standard_weight
        return standard_weight

    elif gender == "other":
        print "Sorry! Don't support other yet!"
        return "Please run the Script again!"
    
    else:
        print "Please input the right gender!"
        return "Please run the Script again!"

print "Welcome to the Standard Weight Program"

result = standard_weight()

print result
