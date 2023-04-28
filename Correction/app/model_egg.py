import re
from pydantic import BaseModel, validator


class ModelEgg(BaseModel):
    breeding: str
    color: str
    immat: str

    @validator("immat")
    def control_length(cls, value):
        """Controls the length of the registration."""
        if len(value) != 12:
            raise ValueError("Registration's should be composed of 12 characters")
        return value

    @validator("immat")
    def control_registration_weight(cls, value):
        weight = value[0:2]
        if not weight.isnumeric() or not (int(weight) % 5 != 0):
            raise ValueError("Registration's weight is incorrect")
        return value

    @validator("immat")
    def control_registration_dash(cls, value):
        char = value[2]
        if char != "-":
            raise ValueError("Registration's dash not found")
        return value

    @validator("immat")
    def control_registration_country(cls, value):
        countries = ["FR", "BE", "AL", "LU", "SU", "IT", "ES"]
        country = value[3:5]
        if not country.isalpha() or country not in countries:
            raise ValueError("Registration's country is incorrect")
        return value

    @validator("immat")
    def control_registration_code(cls, value):
        code = value[5:8]
        if not code.isalpha() or code[0] == code[2]:
            raise ValueError("Registration's code is incorrect")
        return value

    @validator("immat")
    def control_registration_day(cls, value):
        day = value[8:10]
        if not day.isnumeric() or int(day) <= 0 or int(day) > 31:
            raise ValueError("Registration's day is incorrect")
        return value

    @validator("immat")
    def control_registration_month(cls, value):
        month_initial = value[10:]

        if not month_initial.isalpha() or month_initial not in (
            "JA",
            "FE",
            "MA",
            "AV",
            "MI",
            "JU",
            "JL",
            "AO",
            "SE",
            "OC",
            "NO",
            "DE",
        ):
            raise ValueError("Registration's month is incorrect")
        return value

    @validator("immat")
    def control_registration_day_month(cls, value):
        day = value[8:10]
        month_initial = value[10:]
        if (day, month_initial) in [
            ("01", "JA"),
            ("02", "FE"),
            ("03", "MA"),
            ("04", "AV"),
            ("05", "MI"),
            ("06", "JU"),
            ("07", "JL"),
            ("08", "AO"),
            ("09", "SE"),
            ("10", "OC"),
            ("11", "NO"),
            ("12", "DE"),
        ]:
            raise ValueError("Registration's day / month value are not compatible")
        return value
