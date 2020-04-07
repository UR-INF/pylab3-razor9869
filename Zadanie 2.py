from array import *

array = array("u")

print('Wpisz elementy, każdy z nich zatwierdź klawiszem ENTER, ostatni element zatwierdź podwójnie klawiszem ENTER')
while True:
    temp = input();
    if temp == '':
        break;
    else:
        array.append(temp)

print('Wpisane elementy to:')
for i in reversed(array):
    print(i)