#!/usr/bin/python
#coding=UTF-8

import datetime

if __name__ == "__main__":
    print (datetime.date.today().strftime("%d/%m/%Y"))

    miyazakiBirthDate = datetime.date(1941, 1, 5)

    print(miyazakiBirthDate.strftime("%d/%m/%Y"))

    miyazakiBirthDate += datetime.timedelta(days=1)

    print (miyazakiBirthDate.strftime("%d/%m/%Y"))

    miyazakFirstBirthday = miyazakiBirthDate.replace(year=miyazakiBirthDate.year + 1)

    print (miyazakFirstBirthday.strftime("%d/%m/%Y"))



