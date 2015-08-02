from pyreact.Reactive import Reactive
from pyreact.RxVar import RxVar
from pyreact.RxUtils import RxUtils
import time
import math

r = Reactive()
x = RxVar(0.0)
integral = RxVar()
derivative = RxVar()

r.connect(integral, [x], RxUtils(x).integrate)
r.connect(derivative, [x], RxUtils(x).differentiate)

sin = math.pi/2.0

while(True):
    x.set(math.sin(sin))
    print str(x.get()) + "\t" + str(integral.get()) + "\t" + str(derivative.get())
    time.sleep(0.1)
    sin += 0.1
