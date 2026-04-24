r=int(input("enter the raduis"))
def area_circumference(r):
    area=3.14*r*r
    circumference=2*3.14*r
    return area,circumference
print(area_circumference(r))