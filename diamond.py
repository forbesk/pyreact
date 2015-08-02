from pyreact.Reactive import Reactive
from pyreact.RxVar import RxVar
from pyreact.RxFunc import RxFunc

r = Reactive()
a = RxVar(10)
b1 = RxVar()
b2 = RxVar()
c = RxVar()

r.connect(b1, [a], lambda : a.get())
r.connect(b2, [a], lambda : a.get() / 10)
r.connect(c, [b1, b2], lambda : b1.get() + b2.get())

print "Output: " + str(c.get())

a.set(5)

print "Output: " + str(c.get())

