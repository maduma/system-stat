# Solaris system stat to graphite

This program basicaly does this 3 task

- Read data from a solaris stat command (e.g zonestat, iostat, ...)
- Transform the value to graphite format (e.g lable value time)
- Send stat to graphite via the nerwork

PRODUCE STAT -> TRANSFORM DATA -> SEND TO GRAPHITE

## Produce the stat
We rely on an external os command to produce the stat
- iostat (disk)
- zonestat (memory, cpu, network per zone) 
- dlstat (network per interface)
- vmstat (cpu)
- ...

The main logic is to run the program with parameters and read the output
produced. Basicaly they are two input in this stage.

### input
- program location
- program argument
### ouput
- character line stream
- period of stat (e.g 60 sec)
