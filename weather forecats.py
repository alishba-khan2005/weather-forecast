print("----WEATHER FORECAST----")



country=str(input("enter your country: "))
city=str(input("enter your city: "))
temp=int(input("enter the temperature: "))
f=(temp*9/5)+32
if 15<= temp >1:
    print("country",country)
    print("city",city)
    print("temp in farenheit is: ",f)
    print("weather: cold ")
    
elif 15<temp >=30:
    print('country:',country)
    print("city",city)
    print("temp in farenheit is: ",f)
    print("weather: moderate")
    
elif 30<temp>=40:
    print("country:",country)
    print("city")
    print("temp in farenheit is: ",f)
    print("weather is hot")
    
elif 40<temp>=50:
    print("country",country)
    print("city",city)
    print("temp in farenheit is: ",f)
    print("weather is extremely hot")
        