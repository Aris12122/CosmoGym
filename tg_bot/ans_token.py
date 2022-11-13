import random
import string

alphabet = string.ascii_letters
alphabet += string.digits

def myHash(text:str):
    hash=0
    for ch in text:
        hash = ( hash*281  ^ ord(ch)*997) & 0xFFFFFFFF
    return hash

def generate_random_string(x):
    random.seed(x)
    rnd = ''.join(random.choice(alphabet) for i in range(20))
    print(rnd)
    return rnd

def get_ans_token(solved, handle):
    hsh = (myHash(handle) * 390729463 + solved * 1895872127837 + 8652937139) % 2663722543
    # print(hsh)
    return generate_random_string(hsh)