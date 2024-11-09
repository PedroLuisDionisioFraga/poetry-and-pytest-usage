class InvalidRoomType(Exception):
    """Exception raised for invalid room types.

    This exception is raised when an invalid room type is provided,
    typically if the room type does not match any predefined types.

    Examples:
        >>> raise InvalidRoomType("Invalid room type provided.")
    """

    pass


class RoomTypeNotAvailable(Exception):
    """Exception raised when a requested room type is unavailable.

    This exception is raised when a room of a specific type is not available
    at the time of booking or checking availability.

    Examples:
        >>> raise RoomTypeNotAvailable("Requested room type is not available.")
    """

    pass


class RoomNotAvailable(Exception):
    """Exception raised when a specific room is not available.

    This exception is used to indicate that a particular room is unavailable,
    generally due to prior bookings or maintenance.

    Examples:
        >>> raise RoomNotAvailable("The selected room is not available.")
    """

    pass


class RoomHasSchedule(Exception):
    """Exception raised when attempting to modify or delete a room with existing schedules.

    This exception is raised if an action is attempted on a room that
    already has scheduled bookings, indicating the room is currently occupied or reserved.

    Examples:
        >>> raise RoomHasSchedule("Room has existing schedules and cannot be modified.")
    """

    pass


class ScheduleCannotBeOverwritten(Exception):
    """Exception raised when attempting to overwrite an existing schedule.

    This exception is used to signal that an operation would overwrite an
    existing schedule, which is not permitted.

    Examples:
        >>> raise ScheduleCannotBeOverwritten("Schedule cannot be overwritten.")
    """

    pass
