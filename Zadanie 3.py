import random
import numpy
from array import *

array = array("f")

i = int(input("Ile liczb chcesz wygenerować:"))

array.extend(numpy.random.uniform(low=-5, high=5, size=i))
numpy.savetxt("result.txt", array, fmt='%f')