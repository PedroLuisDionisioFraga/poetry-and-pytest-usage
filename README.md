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

## Linter
The project uses [flake8](https://flake8.pycqa.org/en/latest/) as linter. To run the linter in all code, execute the following command:
```bash
flake8 .
```
If the linter find a problem, it will show a message with the error.
```bash
./src/Schedule.py:13:3: E303 too many blank lines (2)
./src/Schedule.py:20:1: W391 blank line at end of file
```
Fixing the error manually and when finish, flake8 will not show any message.
