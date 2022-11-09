def calculate_square_area(side: float):
  return side * side

def calculate_rectangle(length: float, width: float):
  return length * width

def calculate_circle(radius: float):
  pi = 3.14
  return radius * pi

def calculate_rhombus(p: float, q: float):
  return p * q / 2

print("""
---------------
Area Calculator
---------------
Select a shape:
""")
selection= input("""
\t'S' - Square
\t'R' - Rectangle
\t'C' - Circle
\t'H' - Rhombus
""")

def calculate_area(selection):
  area = 0

  if selection == "S":
    side = input("""Enter the side:""")
    area = calculate_square_area(float(side))
  elif selection == "R":
    length = input("""Enter the length:""")
    width = input("""Enter the width:""")
    area = calculate_rectangle(float(length), float(width))
  elif selection == "C":
    radius = input("""Enter the radius:""")
    area = calculate_circle(float(radius))
  elif selection == "H":
    p = input("""Enter the p:""")
    q = input("""Enter the q: """)
    area = calculate_rhombus(float(p), float(q))
  else:
    print("Invalid selection - press S, R, C of H")

  return area

def get_shape_name(tag):
  shape = "Unknown"
  if tag == "S":
    shape = "square"
  elif tag == "R":
    shape = "rectangle"
  elif tag == "C":
    shape = "circle"
  elif tag == "H":
    shape = "rhombus"
  return

area = calculate_area(selection)

print(f"The area of the {get_shape_name(selection)} is {area}")
