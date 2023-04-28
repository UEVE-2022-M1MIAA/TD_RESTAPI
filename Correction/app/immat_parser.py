def size_from_immat(immat):
    """ """
    val: int = int(immat[0:2])
    if int(val) < 50:
        res = "Small"
    elif int(val) < 60:
        res = "Medium"
    elif int(val) < 70:
        res = "Large"
    elif int(val) < 80:
        res = "Extra Large"
    else:
        res = "Unknown"
    return res


def day_from_immat(immat):
    """ """
    day = immat[8:10]
    return day


def month_from_immat(immat):
    """ """
    month = immat[10:]
    if month == "JA":
        res = "January"
    elif month == "FR":
        res = "February"
    elif month == "MA":
        res = "March"
    elif month == "AV":
        res = "April"
    elif month == "MI":
        res = "May"
    elif month == "JU":
        res = "June"
    elif month == "JL":
        res = "July"
    elif month == "AO":
        res = "August"
    elif month == "SE":
        res = "September"
    elif month == "OC":
        res = "October"
    elif month == "NO":
        res = "November"
    elif month == "DE":
        res = "December"
    else:
        res = "Unknown"
    return res
