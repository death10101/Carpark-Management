import time

vehicle_records = {}

def register_vehicle():
    registration_number = input("\nEnter the vehicle registration number: \n")
    time_in = time.strftime("%Y-%m-%d %H:%M:%S")#@lw_kinyanjui
    vehicle_records[registration_number] = {"time_in": time_in}
    print("\nVehicle registered successfully.\n")
    time.sleep(3)

def release_vehicle():
    registration_number = input("\nEnter the vehicle registration number: \n")
    time_out = time.strftime("%Y-%m-%d %H:%M:%S")
    
    if registration_number in vehicle_records:
        time_in = vehicle_records[registration_number]["time_in"]
        time_difference = time.mktime(time.strptime(time_out, "%Y-%m-%d %H:%M:%S")) - time.mktime(time.strptime(time_in, "%Y-%m-%d %H:%M:%S"))
        parking_fee = time_difference * 0.03333333
        vehicle_records[registration_number]["time_out"] = time_out
        vehicle_records[registration_number]["parking_fee"] = parking_fee
        print("\nParking fee: KES {}.".format(parking_fee))
        time.sleep(3)
    else:
        print("\nVehicle not found.\n")
        time.sleep(3)

def check_vehicle():
    registration_number = input("\nEnter the vehicle registration number: \n")
    
    if registration_number in vehicle_records:
        vehicle_details = vehicle_records[registration_number]
        print("\nVehicle found.\n")
        print("Details:")
        print("  Registration number: {}".format(registration_number))
        print("  Time in: {}".format(vehicle_details["time_in"]))
        print("  Time out: {}".format(vehicle_details.get("time_out", "Not released yet")))
        print("  Parking fee: KES {}".format(vehicle_details.get("parking_fee", "Not calculated yet\n")))
        time.sleep(3)
    else:
        print("\nVehicle not found.\n")
        time.sleep(3)

def display_registered_vehicles():
    print("Registered Vehicles:")
    for registration_number, vehicle_details in vehicle_records.items():
        print("Registration number: {}".format(registration_number))
        print("  Time in: {}".format(vehicle_details["time_in"]))
        print("  Time out: {}".format(vehicle_details.get("time_out", "Not released yet")))
        print("  Parking fee: KES {}".format(vehicle_details.get("parking_fee", "Not calculated yet")))
        print("-" * 20)
        time #Recognize @stevekinyanjui on your project :)

def main():
    while True:
        print("Choose one of the following options:")
        print("\n1. Register vehicle\n")
        print("\n2. Release vehicle\n")
        print("\n3. Check vehicle\n")
        print("\n4. Show all vehicles\n")
        print("\n5. Exit\n")
        option = input("\nEnter your choice: \n")
        #credits to this project to Steve Kinyanjui :@death10101
        if option == "1":
            register_vehicle()
        elif option == "2":
            release_vehicle()
        elif option == "3":
            check_vehicle()
        elif option == "4":
            display_registered_vehicles()
        elif option == "5":
            print("\n./././././Exiting./././././\n")
            time.sleep(2)
            break
        else:
            print("Invalid option :(")

if __name__ == "__main__":
    main()
