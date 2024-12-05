import time

nemo = ["nemo"]
everyone = ["dory", "bruce", "marlin", "nemo", "gill", "bloat", "nigel", "squirt", "darla", "hank"]
large = ["nemo" for _ in range(100000)]


def find_nemo(array):

    time_one = time.time()
    for name in array:
        if name == "nemo":
            print("Found nemo")
    time_two = time.time()

    time_diff = (time_two - time_one) * 1000
    print(f"{time_diff} millisecond")


find_nemo(large)
