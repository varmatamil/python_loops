car_database = [{
                    "Name":"Swift",
                    "Price":700000,
                    "CC":1,
                    "Model":"Sedan",
                    "launch_year":2009
                },
                {
                    "Name":"Harrier",
                    "Price":2500000,
                    "CC":2,
                    "Model":"Suv",
                    "launch_year":2008
                },
                {
                    "Name":"Scropio-N",
                     "Price":1800000,
                     "CC":1.5,
                     "Model":"SUV",
                     "launch_year":2009
                },
                {
                    "Name":"Fortuner",
                    "Price":4000000,
                    "CC":2,
                    "Model":"SUV",
                    "launch_year":2006
                }]

for x in car_database:
    print("Car name is",x["Name"],"it's price range starts from",x["Price"],"it has a cubic capacity of",x["CC"],"this car is based on",x["Model"],"Model")

z= 0
for x in car_database:
    if x["Model"] == "SUV":
        z+=1
print("This list has",z,"Suv model cars")

y = 0
for x in car_database:
    if x["Model"] == "Sedan":
        y+=1
print("This list has",y,"Sedan model cars")

y = 0

for x in car_database:
    if x["Price"] > y:
        y = x["Price"]
print("Highest price car is ",x["Name"])

y = 0

for x in car_database:
    if x["Price"] < y:
        y = x["Price"]
print("lowest price car is",x["Name"])

cc = 0

for x in car_database:
    if x["CC"] > cc:
        cc = x["CC"]
print(x["Name"],"has the highest CC in the given list")

cc = car_database[0]["CC"]
car_name = ""
for x in car_database:
    if x["CC"] <= cc:
        car_name = x["Name"]

print(car_name,"has lower cc in given list" )



'''
print out list of all suv type based cars 
print out list of all sedan type based cars
'''

suv_cars=[]
for x in car_database:
    if x["Model"] == "SUV":
        suv_cars.append(x["Name"])

print("suv car list is",suv_cars)

sedan_cars=[]

for x in car_database:
    if x["Model"] == "Sedan":
        sedan_cars.append(x["Name"])
print("sedan car list is",sedan_cars)



for x in car_database:
    if x["Model"].upper() == "SUV":
        discount_price = x["Price"] - (x["Price"]/20)
    else:
        discount_price = x["Price"] - (x["Price"]/10)

    x["updated_discount_price"] = discount_price

print(car_database)


'''

print out all the suv that is launched in 2009

'''

for x in car_database:
    if x["launch_year"] == 2009 and x["Model"].upper() == "SUV":
        print(x["Name"])
