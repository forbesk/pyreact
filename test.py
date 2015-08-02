from pyreact.Reactive import Reactive
from pyreact.RxVar import RxVar
from pyreact.RxFunc import RxFunc

x = RxVar(10)
y = RxVar(20)
sum = RxVar()
prod = RxVar()

def sumxy():
    return x.get() + y.get()

def prodxy():
    return x.get() * y.get()
    
r = Reactive()

r.connect(sum, [x, y], sumxy)
r.connect(prod, [x, y], lambda : x.get() * y.get())

print "Sum is " + str(sum.get())
print "Prod is " + str(prod.get())

x.set(5)
y.set(7)

print "Sum is " + str(sum.get())
print "Prod is " + str(prod.get())
