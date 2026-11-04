import GeometricShape

def displayMe(g):
    if isinstance(g, GeometricShape.Circle):
        print(f'Circle with width = {g.get_radius():.2f}', end=' ')
    if isinstance(g, GeometricShape.Rectangle):
            print(f'Rectangle with width = {g.get_perimeter():.2f}\
    & length = {g.get_height():.2f}')
    print(f'\t Area: {g.get_area():.2f}', end=' ')
    print(f'\t Perimeter: {g.get_perimeter():.2f}')



def main():
    
    c = GeometricShape.Circle()
    r = GeometricShape.Rectangle()
    displayMe(c)
    displayMe(r)

main()


