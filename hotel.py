class Room:
    def __init__(self, room_number, room_type, is_reserved=False):
        self.room_number = room_number
        self.room_type = room_type
        self.is_reserved = is_reserved

class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []

    def add_room(self, room_number, room_type):
        room = Room(room_number, room_type)
        self.rooms.append(room)

    def reserve_room(self, room_number):
        for room in self.rooms:
            if room.room_number == room_number and not room.is_reserved:
                room.is_reserved = True
                return True
        return False

    def display_available_rooms(self):
        available_rooms = [room for room in self.rooms if not room.is_reserved]
        if available_rooms:
            print("Available Rooms:")
            for room in available_rooms:
                print(f"Room {room.room_number} - Type: {room.room_type}")
        else:
            print("No available rooms.")

def main():
    hotel = Hotel("Sample Hotel")

    hotel.add_room(101, "Single")
    hotel.add_room(102, "Double")
    hotel.add_room(103, "Suite")

    while True:
        print("\nWelcome to", hotel.name)
        print("1. Reserve a room")
        print("2. Display available rooms")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            room_number = int(input("Enter room number: "))
            if hotel.reserve_room(room_number):
                print("Room reserved successfully.")
            else:
                print("Room not available for reservation.")

        elif choice == "2":
            hotel.display_available_rooms()

        elif choice == "3":
            print("Thank you for using our Hotel Reservation System.")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()