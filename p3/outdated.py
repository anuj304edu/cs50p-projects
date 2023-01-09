import datetime
l = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    try:
        x = input('date: ')
        if ',' in x:
            m, d, y = x.split(sep=' ')
            m = m.lower().title()
            m = l.index(m)+1
            d = d.removesuffix(',')
            d, m, y = int(d), int(m), int(y)
            p = datetime.datetime(y, m, d)
            print('{:%Y-%m-%d}'.format(p))
            break
        else:
            mm, dd, yy = x.split(sep='/')
            mm, dd, yy = int(mm), int(dd), int(yy)
            p = datetime.datetime(yy, mm, dd)
            print('{:%Y-%m-%d}'.format(p))
            break
    except ValueError:
        pass
