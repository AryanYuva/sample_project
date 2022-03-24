import exercise8_15 
exercise8_15.print_models('charu','nihu','natasha')
#exercise 8-16
#second way of importing
from exercise8_15 import print_models
print_models('shumbham','surya','ram charan')

#another way of importing

from exercise8_15 import print_models as pm
pm('mahesh','allu','shruti')

#another way of importing 

import exercise8_15 as E
E.print_models('aaliya','john','akshay')

from exercise8_15 import *
print_models('rajnikant','satrudhan','vivek obroy')

