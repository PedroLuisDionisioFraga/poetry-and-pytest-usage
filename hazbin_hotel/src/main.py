from datetime import datetime

from hazbin_hotel.src.enums.types import RoomTypeEnum
from hazbin_hotel.src.hotel import Hotel
from hazbin_hotel.src.period import Period
from hazbin_hotel.src.room import Room
from hazbin_hotel.src.schedule import Schedule


def hotel_setup() -> Hotel:
    rooms = [
        Room(RoomTypeEnum.FAMILY, 1000, []),
        Room(RoomTypeEnum.DELUXE, 1300, []),
        Room(RoomTypeEnum.SUITE, 1450, []),
    ]

    return Hotel(rooms)


def book_a_room(hotel: Hotel):
    name = input("Whats your name? ")

    rooms = check_hotel_rooms(hotel)
    chosen_room = input("Choose a Room: ")

    try:
        chosen_room = int(chosen_room)
        print()
    except ValueError:
        print("Please enter a valid number.")
        return

    if chosen_room - 1 < len(hotel.rooms):
        available_dates = check_available_dates()
        chosen_date = input("Choose a date: ")

        try:
            chosen_date = int(chosen_date)
            print()
        except ValueError:
            print("Please enter a valid number.")
            return

        if chosen_date - 1 < len(available_dates):
            print(f"Your book has been confirmed! Thank you {name}")

            room = rooms[chosen_room - 1]
            print(f"Room: {room.type.value} - R$ {room.price}")

            date = available_dates[chosen_date - 1]

            room.add_schedule(create_schedule(name, date))
            print(f"Date: {date['start_date'].date()} -> {date['end_date'].date()}\n")

            return

    print("Invalid options.")


def create_schedule(name: str, date: dict):
    period = Period(date["start_date"], date["end_date"])
    schedule = Schedule(name, period)

    return schedule


def get_available_dates():
    date_format = "%d/%m/%Y"

    available_dates = [
        {"start_date": "16/11/2024", "end_date": "19/11/2024"},
        {"start_date": "21/11/2024", "end_date": "26/11/2024"},
        {"start_date": "23/11/2024", "end_date": "27/11/2024"},
    ]

    for date_range in available_dates:
        date_range["start_date"] = datetime.strptime(date_range["start_date"], date_format)
        date_range["end_date"] = datetime.strptime(date_range["end_date"], date_format)

    return available_dates


def check_available_dates() -> list:
    available_dates = get_available_dates()

    print("------ Available Dates ------")
    for index, date in enumerate(available_dates):
        print(f"{index + 1}. {date['start_date'].date()} -> {date['end_date'].date()}")
    print()

    return available_dates


def check_hotel_rooms(hotel: Hotel) -> list:
    print("------ Available Rooms ------")
    for index, room in enumerate(hotel.rooms):
        print(f"{index + 1} - {room.type.value} - R$ {room.price}")
    print()
    return hotel.rooms


if __name__ == "__main__":
    print("Welcome to Hazbin Hotel")

    hotel = hotel_setup()
    need_to_stop = False

    while not need_to_stop:
        print("Choose an option:")
        print("1. Book a room")
        print("2. Check hotel rooms")
        print("3. Check available dates")
        print("4. Exit\n")

        chosen_option = input()

        match chosen_option:
            case "1":
                book_a_room(hotel)
            case "2":
                check_hotel_rooms(hotel)
            case "3":
                check_available_dates()
            case "4":
                need_to_stop = True
            case default:
                print("Option not available")
