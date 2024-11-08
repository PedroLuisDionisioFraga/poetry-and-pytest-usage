class InvalidRoomType(Exception):
    pass


class RoomTypeNotAvailable(Exception):
    pass


class RoomNotAvailable(Exception):
    pass


class RoomHasSchedule(Exception):
    pass


class ScheduleCannotBeOverwritten(Exception):
    pass
