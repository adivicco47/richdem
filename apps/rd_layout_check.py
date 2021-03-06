#!/usr/bin/env python3

import os
import sys

if len(sys.argv)!=2:
  print("Syntax: {0} <LAYOUT FILE>".format(sys.argv[0]))
  sys.exit(-1)

with open(sys.argv[1],'r') as fin:
  layout = fin.readlines()
#except:
#  print("Failed to open layout file!")
#  sys.exit(-1)

commas = layout[0].count(',')
print("Layout height: {0}".format(len(layout)))
print("Layout width: {0}".format(commas+1))

for i in range(len(layout)):
  if layout[i].count(',')!=commas:
    print("Warning: Row {0} had an unexpected with of {1}!".format(i,layout[i].count(',')+1))

layout = [row.split(',') for row in layout]
layout = [x.strip() for row in layout for x in row] #Flatten layout array, stripping whitespace

total_tiles = len(layout)
print("Total tile count: {0}".format(total_tiles))

layout = [x for x in layout if len(x)>0]          #Remove null tiles
print("Null tile count: {0}".format(total_tiles-len(layout)))
print("Data tile count: {0}".format(len(layout)))

path, layout_filename = os.path.split(sys.argv[1])
print("Base path of layout file: {0}".format(path))

if len(layout)!=len(set(layout)):
  print("Warning: Layout contained duplicate filenames!")

for x in layout:
  if not os.path.exists(os.path.join(path,x)):
    print("Warning: File '{0}' does not exist!".format(x))
