import time
ttime=time.localtime()
print(ttime)
print(time.strftime("%a %b %d %H:%M:%S %Z %Y",ttime))
