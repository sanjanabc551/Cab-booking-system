import random
from datetime import datetime


class CabBookingSystem:
    def __init__(self):
        self.users = {}  # phone -> {name, password, bookings}
        self.current_user = None
        self.rate_per_km = 10  # ₹10/km

    def register_user(self):
        print("\n--- Registration ---")
        name = input("Enter your name: ").strip()
        phone = input("Enter your phone number: ").strip()
        password = input("Create a password: ").strip()

        if phone in self.users:
            print("User already exists with this phone number!")
            return False

        self.users[phone] = {
            'name': name,
            'password': password,
            'bookings': []
        }
        print("Registration successful! Please login.")
        return True

    def login(self):
        print("\n--- Login ---")
        phone = input("Enter your phone number: ").strip()
        password = input("Enter your password: ").strip()

        user = self.users.get(phone)
        if user and user['password'] == password:
            self.current_user = phone
            print(f"Welcome back, {user['name']}!")
            return True
        else:
            print("Invalid phone number or password!")
            return False

    def book_cab(self):
        if not self.current_user:
            print("Please login first!")
            return

        print("\n--- Book a Cab ---")
        pickup = input("Enter pickup location: ").strip()
        drop = input("Enter drop location: ").strip()

        # Simulate random distance between 1-20 km
        distance = random.randint(1, 20)
        fare = distance * self.rate_per_km

        booking = {
            'pickup': pickup,
            'drop': drop,
            'distance': distance,
            'fare': fare,
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        self.users[self.current_user]['bookings'].append(booking)

        print("\nBooking confirmed!")
        print(f"From: {pickup}")
        print(f"To: {drop}")
        print(f"Distance: {distance} km")
        print(f"Fare: ₹{fare}")
        print(f"Time: {booking['timestamp']}")

    def view_booking_history(self):
        if not self.current_user:
            print("Please login first!")
            return

        bookings = self.users[self.current_user]['bookings']
        print("\n--- Your Booking History ---")

        if not bookings:
            print("No bookings found!")
            return

        for i, booking in enumerate(bookings, 1):
            print(f"\nBooking #{i}")
            print(f"From: {booking['pickup']}")
            print(f"To: {booking['drop']}")
            print(f"Distance: {booking['distance']} km")
            print(f"Fare: ₹{booking['fare']}")
            print(f"Time: {booking['timestamp']}")

    def logout(self):
        self.current_user = None
        print("Logged out successfully!")

    def run(self):
        print("=== Welcome to Cab Booking System ===")

        while True:
            print("\n--- Main Menu ---")
            if not self.current_user:
                print("1. Register")
                print("2. Login")
                print("4. Exit")
            else:
                print("1. Book a Cab")
                print("2. View Booking History")
                print("3. Logout")
                print("4. Exit")

            choice = input("Enter your choice: ").strip()

            if not self.current_user:
                if choice == '1':
                    self.register_user()
                elif choice == '2':
                    self.login()
                elif choice == '4':
                    print("Thank you for using our service!")
                    break
                else:
                    print("Invalid choice! Please try again.")
            else:
                if choice == '1':
                    self.book_cab()
                elif choice == '2':
                    self.view_booking_history()
                elif choice == '3':
                    self.logout()
                elif choice == '4':
                    print("Thank you for using our service!")
                    break
                else:
                    print("Invalid choice! Please try again.")


if __name__ == "__main__":
    system = CabBookingSystem()
    system.run()
