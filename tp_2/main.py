import agent
import random as rand
import string
import time
import sys

if __name__ == "__main__":
    a = agent.Agent()
    while True:
        a.live();
        time.sleep(.5)