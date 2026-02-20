def format_conversion(s):
    period = s[-2:]
    time_part = s[:-2]
    hh, mm, ss = time_part.split(":")
    
    hh = int(hh)

    if period == "PM" and hh != 12:
        hh += 12
    elif period == "AM" and hh == 12:
        hh = 0

    return f"{hh:02}:{mm}:{ss}"

s = "07:05:45PM"
format_conversion(s)