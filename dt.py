import datetime
currentdate = datetime.date(2006,1,1)
enddate = datetime.date(2006,3,31)
while currentdate <= enddate:
   #print currentdate
   yyyymmdd=currentdate.strftime("%Y/%m/%d")
   ddmmyyyy=yyyymmdd[8:]+"/"+yyyymmdd[5:7]+"/"+yyyymmdd[:4]
   print(ddmmyyyy)
   currentdate += datetime.timedelta(days=1)
