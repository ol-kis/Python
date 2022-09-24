import math
coordinates_A_x=float(input("enter coordinates A (x): "))
coordinates_A_y=float(input("enter coordinates A (y): "))
coordinates_B_x=float(input("enter coordinates B (x): "))
coordinates_B_y=float(input("enter coordinates B (y): "))
distance=round(math.sqrt((coordinates_B_x-coordinates_A_x)**2 +(coordinates_B_y-coordinates_A_y)**2),4)
print(f'distance between points: {distance}')