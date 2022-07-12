# https://www.codewars.com/kata/52742f58faf5485cae000b9a/train/python

def format_duration(seconds):
    years_total = seconds // 60 // 60 // 24 // 365
    days = (seconds // 60 // 60 // 24) % 365
    hours = (seconds // 60 // 60) % 24
    minutes = (seconds // 60) % 60
    seconds_final = seconds % 60
    result = []
    result_str = ""

    if seconds <= 0:
        return "now"
    else:
        if years_total == 1:
            result.append("1 year")
        elif years_total > 0:
            result.append("{} years".format(years_total))
        if days == 1:
            result.append("1 day")
        elif days > 0:
            result.append("{} days".format(days))
        if hours == 1:
            result.append("1 hour")
        elif hours > 0:
            result.append("{} hours".format(hours))
        if minutes == 1:
            result.append("1 minute")
        elif minutes > 0:
            result.append("{} minutes".format(minutes))
        if seconds_final == 1 and minutes != 0:
            result.append("1 second")
        elif seconds == 1:
            return "1 second"
        elif seconds_final == 0:
            pass
        else:
            result.append("{} seconds".format(seconds_final))

    for index, string in enumerate(result):
        if index == (len(result)) - 1 and index > 0:
            result_str += " and " + result[index]
        elif index == 0:
            result_str += result[0]
        else:
            result_str += ", " + result[index]

    return result_str


print(format_duration(62))
