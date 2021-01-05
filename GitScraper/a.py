
oldtime = '2020-12-06'
datetimeobject = datetime.strptime(oldtime,'%Y-%m-%d')
DateCreated = datetimeobject.strftime('%Y%m%d')
print(DateCreated)

date_format = "%Y%m%d"
DateNow = '202111'

a = datetime.strptime(DateCreated, date_format)
b = datetime.strptime(DateNow, date_format)
delta = b - a
print (delta.days) # that's it
