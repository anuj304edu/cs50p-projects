time = input('what time it is? ')

if 'a.m.' in time:
    time = time.removesuffix('a.m.')
    hours, minutes = time.split(":")
elif 'p.m.' in time:
    time = time.removesuffix('p.m.')
    hours, minutes = time.split(":")
    hours = int(hours)+12
else:
    hours, minutes = time.split(":")

def main():
    re = convert(time)
    if 7.0<= re <=8.0:
        print('breakfast time')
    elif 12.0<= re <=13.0:
        print('lunch time')
    elif 18.0<= re <=19.0:
        print('dinner time')



def convert(time):
    m = int(minutes)
    h = int(hours)
    if m >= 60:
        mi = m//60
        ho = h+mi
        m = (m%60)/60
        re = (float(ho) + float(m))
        return re
    else:
        m = m/60
        re = (float(h) + float(m))
        return re

main()