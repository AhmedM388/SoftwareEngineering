#this program works out holiday cost using 4 separate functions and dictionaries
rental_days = int(input("How many days do you want to rent a car")) #input number of days to rent car
city_flight = input("Which city will you be flying to, Dubai,London,Sydney or New York") #input city 
num_nights = int(input("How many nights are you planning to stat for")) #input number of days to visit city
hotel_price = 0
flight_price = 0
car_price = 0
holiday_cost2 = 0
cities = ["Dubai","London","Sydney","New York"] #creates a list of cities
hotelprices_dict = {"Dubai":100,"Sydney":120,"New York":130,"London":99} #creates a dictionary of hotel prices based on location
flightprices_dict = {"London":200,"Dubai":600,"Sydney":1100,"New York":800} #creates a dictionary of flight prices based on location
carprices_dict = {"Dubai":30,"Sydney":40,"New York":80,"London":65} #creates a dictionary of car prices based on location

def hotel_cost(): #creates function
    global hotel_price
    hotel_price = num_nights * hotelprices_dict[city_flight] #works out hotel price using city location and number of nights 
    
    print(f'The hotel price  will be £{hotel_price}')
def plane_cost():
    global flight_price
    flight_price = flightprices_dict[city_flight]
    print(f'The flight price will be £{flight_price}')

def car_rental():
    global car_price
    car_price = rental_days * carprices_dict[city_flight]
    print(f'The rental price for the car  will be £{car_price}')


def holiday_cost(): #calls all the other functions into the holiday function
    hotel_cost()
    plane_cost()
    car_rental()
    holiday_cost2 = car_price + hotel_price +flight_price
    print(f'The total price of the holiday is £{holiday_cost2}')


holiday_cost()



