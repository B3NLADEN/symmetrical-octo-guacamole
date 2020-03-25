#!/usr/bin/python


import packagedemo


x = packagedemo.quickAdd(10,10) 

print x

ins = packagedemo.Calculator(20,20)
y = ins.add()
print y

print '%d' % ins.divide()
