#!/usr/bin/env python

log = open('log', 'r')
context_switch_time = open('context_switch_time.txt', 'w')
lines = log.readlines()

for line in lines :
    line = line.strip()
    inst, args = line.split(' ', 1)

    if inst == 'switch' :
        dummy, dummy, dummy, tick_reload, out_minitick, in_minitick = args.split(' ')
        context_switch_time.write( '%f\n' % ((float(out_minitick) - float(in_minitick)) / float(tick_reload)) );


