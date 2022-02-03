
import datetime

def run():
    #datetime now toma la hora local
    my_time = datetime.datetime.now()
    print(my_time)
    print(my_time.strftime('%I:%M %p'))
    # dato today me trae solo la fecha actual
    my_time_ = datetime.date.today()
    print(my_time_)
    print(my_time.year)
    print(my_time.month)
    print(my_time.day)

    print()
    #datetime utcnow toma la hora global y es mejor
    my_time_2 = datetime.datetime.utcnow()
    print(my_time_2)
    print(my_time_2.strftime('%I:%M %p'))

if __name__=='__main__':
    run()