#Qestion 1 ( Flight class)

class Flight():
    def __init__(self, flight_no, source, destination, base_fare):
        self.flight_no = flight_no
        self.source= source
        self.destination=destination
        self.base_fare=base_fare
        
    def get_flight_info(self):
        return f"Your flight number is {self.flight_no}, from {self.source} to {self.destination}"
    
    def calculate_fare(self,passenger_count,discount_percent):
        self.passenger_count = passenger_count
        self.discount_percent = discount_percent
        if self.passenger_count >=4:
            total_fare= self.base_fare * self.passenger_count
            return total_fare
        
        discounted_price = total_fare * self.discount_percent/100
        
        print (f" Total discounted fare for {self.passenger_count} passengers is {discounted_price}")

    def update_route(self, new_source=None, new_destination=None):
        if new_source and new_destination:
            self.source=new_source
            self.destination=new_destination
        elif new_destination:
            self.destination=new_destination



KikAirlines = Flight("PKJ543", "Calicut", "Bengaluru", 2000)
print(KikAirlines.get_flight_info())
fare1 = KikAirlines.calculate_fare(4, 10)
print(fare1)

KikAirlines.update_route(new_destination="Kochi")
print ("After updating destination:",KikAirlines.get_flight_info())
KikAirlines.update_route(new_source="Mumbai", new_destination="Chennai")
print ("After updating source and destination:",KikAirlines.get_flight_info())
