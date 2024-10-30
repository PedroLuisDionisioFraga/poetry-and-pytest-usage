# Seminar of Software Engineer
Basic project that implement tests with [Pytest](https://docs.pytest.org/en/stable/) and poetry dependence manager into a hotel reservation system.

## Team
- Pedro Luis
- Arthur Bueno
- Pedro Augusto
- Marcos Henrique

## Requirements
- Chrome extension to view mermaid diagrams: [Mermaid Previewer](https://chromewebstore.google.com/detail/mermaid-previewer/oidjnlhbegipkcklbdfnbkikplpghfdl?utm_source=ext_app_menu)
- Python 3.12

## Architecture
```mermaid
classDiagram
    class Room {
        - int number
        - string type
        - float price
        - list~Schedule~ schedules
        + get_number() int
        + get_type() string
        + get_room_price() float
        + update_schedule() bool
        + update_price(new_price: float) bool
        + add_schedule(schedule: Schedule) bool
        + is_period_available(period: Period) bool
    }

    class Schedule {
        - int id
        - string client_name
        - Room room
        - Period period
        + get_client_name() string
        + get_room() Room
        + reserve_room(room: Room, period: Period) bool
    }

    class Period {
        - Date start_date
        - Date end_date
        + update_start_date() bool
        + update_end_date() bool
    }

    Room "1" <-- "*" Schedule : "associates with"
    Schedule "*" --> "1" Period
```
