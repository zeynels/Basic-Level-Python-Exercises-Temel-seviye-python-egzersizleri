from datetime import datetime

# simdi = datetime.now()
# result = datetime.today()
# simdi = datetime.now().year
# simdi = datetime.now().month
# simdi = datetime.now().day
# simdi = datetime.now().hour

# simdi = datetime.ctime(result)

# simdi = datetime.strftime(result, '%Y')
# simdi  = datetime.strftime(result, '%X')
# simdi = datetime.strftime(result, '%d')

# t = "5 nisan 2019 hour 10:12:30"
# result=datetime.strptime(t, '%d %B %Y hour %H:%M:%S')

# result = result.year
# print(result)
t = "5 may 2019 hour 10:12:30"
result=datetime.strptime(t, '%d %B %Y hour %H:%M:%S')
result = result.year
print(result)

birthday = datetime(1983,5,9)
# gun, ay, yil = t.split()
# print(gun)
# print(ay)
# print(yil)

# print(simdi)