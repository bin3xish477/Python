#!/usr/bin/env python3

try:
  # --> import os for performing os functions
  import os
  # --> import sqlite3 storing our csv file data into a database
  import sqlite3
  # --> import csv for parsing our csv file
  import csv
  # --> import colored for creeating a nicer looking interface
  import colored
# --> handling an importing module error
except ImportError:
  print('%s[-] Error importing module%s' % (fg(1),attr(0)))
