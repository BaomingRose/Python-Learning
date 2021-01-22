from datetime import datetime, timedelta,timezone
import time

if __name__ == '__main__':
    now = datetime.now()
    print(now)          # 2020-06-15 09:51:18.990352
    print(type(now))    # <class 'datetime.datetime'>

    dt = datetime(2020, 6, 15, 10, 10)
    print(dt)

    # 把1970年1月1日 00:00:00 UTC+00:00时区的时刻称为epoch time，记为0，
    # 当前时间就是相对于epoch time的秒数
    print(dt.timestamp())       # 把datetime转换为timestamp，有小数位，小数位表示毫秒数

    t = 1592187000.0
    print(datetime.fromtimestamp(t))    # timestamp转换为datetime(本地时间)
    print(datetime.utcfromtimestamp(t))     # UTC时间

    cday = datetime.strptime('2020-6-15 10:35:00', '%Y-%m-%d %H:%M:%S')     # str转换为datetime
    print(cday)
    print(type(cday))

    # datetime转换为str
    # print(now.strptime('%a, %b %d %H:%M'))

    # datetime的加减，需要借助timedelta类，使用timedelta你可以很容易地算出前几天和后几天的时刻
    print(now + timedelta(days=100))
    print(now - timedelta(hours=36))
    print(now - timedelta(days=2, hours=12))

    # 本地时间转换为UTC时间，北京时间是UTC+8:00时区的时间，而UTC时间指UTC+0:00时区的时间
    tz_utc_8 = timezone(timedelta(hours=8))  # 创建时区UTC+8:00
    dt = now.replace(tzinfo=tz_utc_8)       # 强制设置为UTC+8:00
    print(dt)
