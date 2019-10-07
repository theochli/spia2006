import os
total_secs = 7684
hours = total_secs // 3600
secs_still_remaining = total_secs % 3600
minutes =  secs_still_remaining // 60
secs_finally_remaining = secs_still_remaining  % 60
L = [15,'abc', (42, 'fizzbuzz')]
print (hours, 'hours', minutes, 'minutes', secs_finally_remaining, 'seconds')
