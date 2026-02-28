#question 2 (Flight ticket procesing Module)

flight_no = "AI203"
base_fare= "4500.75"
tax_percent= "5"
seat_number = "12A,12B, 14C, 15D"
is_international ="True"

#a) 
base_fare = float(base_fare)
tax_percent= float(tax_percent)

final_fare= base_fare + (base_fare*tax_percent/100)
print ("Final fare is", final_fare)

#b)
seat_list = seat_number.split(",")
print("Seat List:", seat_list)

#c)
seat_set = set(seat_list)
print("The seat list is converted into a set:", seat_set)

#d)
is_international=bool(is_international == "True")
print ("Now it is a proper boolean value, Is international ?", is_international)

#e)
flight_summary = {

    "flight_no" : flight_no,
    "final fare" : int(final_fare),
    "seat_number" : tuple(seat_list)
}
