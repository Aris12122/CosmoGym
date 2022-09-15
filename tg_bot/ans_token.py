import random
import string

alphabet = string.ascii_letters
alphabet += string.digits

def generate_random_string(x):
    random.seed(x)
    rnd = ''.join(random.choice(alphabet) for i in range(20))
    print(rnd)
    return rnd

def get_ans_token(contest, solved, handle):
    hsh = (hash(handle) * 390729463 + solved * 1895872127837 + contest * 15986049132439) % 2663722543
    print(hsh)
    return generate_random_string(hsh)