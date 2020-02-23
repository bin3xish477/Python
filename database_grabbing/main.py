#!/usr/bin/env python3

try:
  import os
  import sqlite3
  import argparse
  import colored
except ImportError:
  print('%s[-] Error importing module %s' % (fg(1),attr(0)))
