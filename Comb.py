import sympy as sp

# Defining Symbols
x, y, z = sp.symbols("x y z")

# Function to find the directional derivative along a vector
def along_the_vector(eq, wrt_x, wrt_y, wrt_z, pt1, pt2, pt3):
    print("Enter the vector:")
    vec1 = int(input("i = "))
    vec2 = int(input("j = "))
    vec3 = int(input("k = "))

    # Directional derivative formula
    dd = (wrt_x * vec1 + wrt_y * vec2 + wrt_z * vec3) / sp.sqrt(vec1 ** 2 + vec2 ** 2 + vec3 ** 2)

    # Substituting the point into the directional derivative formula
    dd_at_point = dd.subs({x: pt1, y: pt2, z: pt3})

    print("Directional derivative along the vector:", sp.simplify(dd_at_point))


# Function to find the directional derivative toward a point
def toward_the_point(eq, wrt_x, wrt_y, wrt_z, pt1, pt2, pt3):
    print("Enter the point toward which you want to find the directional derivative:")
    toward_pt1 = int(input("Point 1: "))
    toward_pt2 = int(input("Point 2: "))
    toward_pt3 = int(input("Point 3: "))

    # Directional derivative formula
    dd = wrt_x * (toward_pt1 - pt1) + wrt_y * (toward_pt2 - pt2) + wrt_z * (toward_pt3 - pt3)
    dd /= sp.sqrt((toward_pt1 - pt1) ** 2 + (toward_pt2 - pt2) ** 2 + (toward_pt3 - pt3) ** 2)

    print("Directional derivative toward the point:", sp.simplify(dd))


# Main loop
while True:
    print("Menu")
    print("1. Along the vector")
    print("2. Toward the point")
    print("3. Exit")
    user_choice = int(input("Enter your choice: "))

    if user_choice == 3:
        break

    # Input equation
    eq = sp.sympify(input("Enter the equation: "))

    # Input point
    pt1 = int(input("Point 1: "))
    pt2 = int(input("Point 2: "))
    pt3 = int(input("Point 3: "))

    # Calculate partial derivatives
    wrt_x = sp.diff(eq, x)
    wrt_y = sp.diff(eq, y)
    wrt_z = sp.diff(eq, z)

    if user_choice == 1:
        along_the_vector(eq, wrt_x, wrt_y, wrt_z, pt1, pt2, pt3)
    elif user_choice == 2:
        toward_the_point(eq, wrt_x, wrt_y, wrt_z, pt1, pt2, pt3)
