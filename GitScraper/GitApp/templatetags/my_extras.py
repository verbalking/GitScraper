from django import template
from datetime import date, datetime


register = template.Library()

#This function is calculating the number of days passed since the repo was created
#It starts by formating the date to this format (%Y%m%d),
#and it calculates the difference and returns the number of days passed

def calculateTime(oldtime):

    #We exctract the date from the item.created_at, because it contains additional data that we do not need
    oldtime=oldtime[:10]

    #conversion from %Y-%m-%d to %Y%m%d
    datetimeobject = datetime.strptime(oldtime,'%Y-%m-%d')
    DateCreated = datetimeobject.strftime('%Y%m%d')
    date_format = "%Y%m%d"

    #curren date with the same format
    DateNow = '202115'

    a = datetime.strptime(DateCreated, date_format)
    b = datetime.strptime(DateNow, date_format)
    delta = b - a
    return (delta.days)

#we register our filter, so it would be used in an html file with a simple calculateTime call
register.filter('calculateTime',calculateTime)
