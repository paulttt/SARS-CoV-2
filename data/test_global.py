import time
updating=True
def yo():
    while updating:
        print('still updating')
        time.sleep(1)
def stop():
    updating = False

if __name__ == "__main__":
    yo()
    time.sleep(4)
    stop()