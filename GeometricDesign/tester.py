import GeometricShape

def main():
    x = GeometricShape.GeometricObject()
    print(x)
    z = GeometricShape.GeometricObject('Blue', False)
    print(z)

    c = GeometricShape.Circle()
    c.set_radius(20)
    print(c)
   
    
main()