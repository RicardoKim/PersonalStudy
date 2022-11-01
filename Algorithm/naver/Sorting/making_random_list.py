import random 

def random_list():
    length = random.randint(10, 100)
    unsorted_list = random.sample(range(1,101), 8) 
    return unsorted_list