# Question: Write a function that will return the number of days in a month (not using system date time library)

def calendar():
    month = [
                'January',
                'February',
                'March',
                'April',
                'May',
                'June',
                'July',
                'August',
                'September',
                'October',
                'November',
                'December'
            ]
    for i in month:
        if i == 'February':
            print "February: 28 days"
        elif month.index(i)%2 != 0:
            print i+"="+"30 days"
        else:
            print i+"="+"31 days"

calendar()
