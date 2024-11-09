from enum import Enum


class RoomTypeEnum(Enum):
    SINGLE = "SINGLE"  # Single bed for one guest.
    DOUBLE = "DOUBLE"  # Room with a double bed for two guests.
    TWIN = "TWIN"  # Two single beds for two guests.
    SUITE = "SUITE"  # Larger room with luxury amenities.
    FAMILY = "FAMILY"  # Larger room for families, often with extra beds.
    DELUXE = "DELUXE"  # Higher-end room with added comfort or space.
    STUDIO = "STUDIO"  # Open-plan room with living and sleeping area.
    PRESIDENTIAL_SUITE = "PRESIDENTIAL_SUITE"  # Top-tier suite with premium amenities.
    BUNGALOW = "BUNGALOW"  # Stand-alone unit, often with private outdoor space.
    PENTHOUSE = "PENTHOUSE"  # Luxurious top-floor suite with exclusive views.


ROOM_MULTIPLIERS = {
    RoomTypeEnum.SINGLE: 1.0,  # Base rate for single occupancy.
    RoomTypeEnum.DOUBLE: 1.5,  # Moderate rate for two guests.
    RoomTypeEnum.TWIN: 1.4,  # Slightly lower rate for twin beds.
    RoomTypeEnum.SUITE: 2.0,  # Higher rate for luxury.
    RoomTypeEnum.FAMILY: 1.8,  # Larger room for families.
    RoomTypeEnum.DELUXE: 1.6,  # Enhanced comfort or space.
    RoomTypeEnum.STUDIO: 1.3,  # Open-plan living space.
    RoomTypeEnum.PRESIDENTIAL_SUITE: 3.0,  # Premium rate for top suite.
    RoomTypeEnum.BUNGALOW: 2.2,  # Private unit with outdoor area.
    RoomTypeEnum.PENTHOUSE: 3.5,  # Highest rate for exclusive amenities.
}
