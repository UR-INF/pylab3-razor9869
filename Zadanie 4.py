import numpy


def arr(first_row):
    size = len(first_row)
    array = numpy.zeros((size, size), dtype=numpy.longlong);
    array[0] = first_row

    for i in range(1, size):
        array[i] = numpy.power(array[i - 1], 2)

    return array


first_row = (2, 3, 4, 5, 6)
print(arr(first_row))
