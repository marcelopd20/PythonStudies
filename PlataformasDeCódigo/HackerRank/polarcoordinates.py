from cmath import polar
x = input()
for y in polar(complex(complex(x).real, complex(x).imag)):
    print(y)