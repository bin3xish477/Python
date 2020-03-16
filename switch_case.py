#!/usr/bin/env python3


import random


def dow_switch(day_num:int):
  dict_dow = {
      1: lambda: print('Monday'),
      2: lambda: print('Tuesday'),
      3: lambda: print('Wednesday'),
      4: lambda: print('Thursday'),
      5: lambda: print('Friday'),
      6: lambda: print('Saturday'),
      7: lambda: print('Sunday')
  }


def main():
  day_num = random.randint(1,7)
  print('Day of the week is: ', day_num)


if __name__ == '__main__':
    main()