import time

count = 0
max_count = 10000
while True:
    print ("We are at count {}.".format(count))
    count += 1
    if count >= max_count:
        print ("Shutdown.")
        break
    time.sleep(1)