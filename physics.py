def area_of_circle ():
    radius = float(input("Enter radius"))
    area = 2 * 22/7 * radius
    print (area)
#area_of_circle()




def calculate_velocity():
    displacement = float(input("Enter displacement"))
    time = int(input("Enter Time"))
    velocity = displacement/time
    print(velocity)
#calculate_velocity()


print ("Welcome to Tactical Operations Solver")

print ("We offer assistance with both Physics and Mathematics Operations")

print ("To calculate for the following equations choose the appropriate letter")



#print("Options")
print("A = Calculate the Speed of a Body in Motion")
print("B = Calculate the Area of a Parallelogram ")
print("C = Calculate the Time of Flight")
print("D = Calculate the Area of Trapezium")
print("E = Calculate the Force acting on an object ")
options = {"A" : "Calculate the Speed of a Body in Motion" ,
                  "B" : "Calculate the Area of a Parallelogram ",
                        "C" : "Calculate the Time of Flight",
                              "D" : "Calculate the Area of Trapezium",
                                    "E" : "Calculate the Force acting on an object "}




def a ():
    distance = float(input("Enter Distance"))
    time = int(input("Enter Time"))
    a = distance/time
    print(a)
#a()


def b ():
    base = int(input("Enter Base"))
    height = int(input("Enter Height"))
    b = base * height
    print(b)
#b()




def c ():
    u = int(input("Enter Initial Velocity"))
    import math
    angle_in_radians = math.pi/2 # 90 degrees
    sine_value = math.sin(angle_in_radians)
    sine_value = float(input("Enter value of Sine"))
    g = int(input("Enter Acceleration due to gravity "))
    c = 2 * u* sine_value/g
    print(c)
#c()





def d ():
    a = float(input("Enter first length of parallel side"))
    b = float(input("Enter second length of parallel side"))
    height = float(input("Enter Height"))
    d = 1/2 * (a+b) *height
    print(d)
#d()




def e():
    mass = float(input("Enter Mass"))
    acceleration = float(input("Enter acceleration "))
    e = mass * acceleration
    print(e)
#e()


def main():
        choice = input("Enter your choice: ")
        if choice == "a":
            a()
        if choice == "b":
            b()
        if choice == "c":
            c()
        if choice == "d":
            d()
        if choice == "e":
            e()
if __name__ == '__main__' :
    main()
