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

## Installation
To get started, you need to install Poetry. You can do this by following the instructions [here](https://python-poetry.org/docs/#installation).
After installing Poetry, follow the steps below to install the project's dependencies:

### Clone the repository
```bash 
git clone https://github.com/PedroLuisDionisioFraga/poetry-and-pytest-usage.git
cd poetry-and-pytest-usage
```

### Install the project dependencies 
```bash
poetry install
```

## Running the Project
To run the project, use the command:
```bash
poetry run python path/to/your/main.py
```

## Architecture
```mermaid
classDiagram
    class Room {
        - int number
        - string type
        - float price
        - float multiplier_factor_price
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
    }

    class Period {
        - Date start
        - Date end
        + change_start() bool
        + change_end() bool
    }

    class Hotel { 
        - list~Room~ rooms 
        + get_rooms() list~Room~ 
        + add_room(room: Room) bool 
        + remove_room(room: Room) bool 
        + check_room_type_availability(room_type: RoomTypeEnum) Room | None 
        + schedule_a_room(client_name: string, room_type: RoomTypeEnum, start_date: Date, end_date: Date) bool 
    } 
    
    Room "1" <-- "*" Schedule : "associates with" 
    Schedule "*" --> "1" Period 
    Hotel "1" --> "*" Room : "manages"
```

## Code Quality


### Linter
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

### Formatter
The project uses [black](https://black.readthedocs.io/en/stable/) as formatter. To run the formatter in all code, execute the following command:
```bash
black .
```

### Sorting Imports
The project uses [isort](https://pycqa.github.io/isort/) as sorting imports. To run the sorting imports in all code, execute the following command:
```bash
isort .
```

### Resume
- **Black**: A code formatter that applies consistent style across your code automatically.
- **isort**: Organizes and sorts imports to keep them clean and PEP 8-compliant.
- **Flake8**: A linter that checks for syntax errors, potential bugs, and style violations.

### Documentation

- **GitHub Pages**: https://pedroluisdionisiofraga.github.io/poetry-and-pytest-usage/

### Release

- **PyPi**: https://pypi.org/project/hazbin-hotel/