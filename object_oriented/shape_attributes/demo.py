import geometric_shape

def main():
    x = geometric_shape.GeometricShape()
    print(x)
    z = geometric_shape.GeometricShape('Blue', False)
    print(z)

    c = geometric_shape.Circle()
    c.set_radius(20)
    print(c)

if __name__ == "__main__":
    main()
