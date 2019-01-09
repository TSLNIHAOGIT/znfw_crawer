# import time
# t1=time.strftime("%Y-%m-%d %H:%M:%S")#获取当前时间
#
#
# thisTime = "2016-07-31"
# timeTuple = time.strptime(thisTime, "%Y-%m-%d")
# time.strftime("%Y-%m-%d ",timeTuple)
# print(t1,timeTuple,thisTime)




from datetime import date, timedelta

def gen_dates(bdate, days):
    day = timedelta(days=1)
    for i in range(days):
        yield bdate + day*i

def month_computer(year,month):
    year_1=year
    month_1=month

    while True:
        if month_1==13:
            year_1=year_1+1
            month_1=1
            m='0'+str(month_1)
            print(year_1,m)
        else:
            if month_1<=9:
                m='0'+str(month_1)
                print(year_1,m)
            else:
                print(year_1,month_1)
        month_1 = month_1 + 1
        if year_1==2017 and month_1>11:
            break



if __name__ == '__main__':
    # bdate = date(2013, 6, 1)
    # for d in gen_dates(bdate, 31):
    #     print(d)
    # print(date(2016, 6, 1)>date(2006, 6, 1))

    month_computer(2013,6)

