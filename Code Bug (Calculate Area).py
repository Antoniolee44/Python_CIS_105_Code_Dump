def calculate_area(radius):
    pi = 3.14
    area = pi * radius * radius
    return area


radius_input = input("enter the radius of a circle: ")
try:  # use a try/except block in order to handle exceptions
    radius = int(radius_input)
    circle_area = calculate_area(radius)
    print("the area of the circle is: ", circle_area)
except ValueError:
    print('Invalid input: Radius must be an integer')
except Exception as e:
    print('an error has occurred: ', str(e))
