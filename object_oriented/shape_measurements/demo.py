import geometric_shape

def displayMe(g):
    if isinstance(g, geometric_shape.Circle):
        print(f'Circle with radius = {g.get_radius():.2f}', end=' ')
    if isinstance(g, geometric_shape.Rectangle):
            print(f'Rectangle with width = {g.get_width():.2f}\
    & height = {g.get_height():.2f}')
    print(f'\t Area: {g.get_area():.2f}', end=' ')
    print(f'\t Perimeter: {g.get_perimeter():.2f}')



def main():

    c = geometric_shape.Circle()
    r = geometric_shape.Rectangle()
    displayMe(c)
    displayMe(r)

if __name__ == "__main__":
    main()
