
'''

long map(long x, long in_min, long in_max, long out_min, long out_max) {
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
}

def my_map(x, in_min, in_max, out_min, out_max):
    return int((x-in_min) * (out_max-out_min) / (in_max-in_min) + out_min)

def valmap(value, istart, istop, ostart, ostop):
  return ostart + (ostop - ostart) * ((value - istart) / (istop - istart))

'''

def Alema1map(valor, in_min, in_max, out_min, out_max):
    return int((valor-in_min) * (out_max-out_min) / (in_max-in_min) + out_min)

print(Alema1map(239, 0, 480, 0, 255))
