import agent
import random as rand
import string
import time
import sys

BORED_IN = 3
HAPPY, SAD, BORED = ':-)', ':-(', ':-Z'
STATES = [HAPPY, SAD, BORED]
ACTIONS = ['1', '2']#['A', 'B', 'C', 'D', 'E']
FEEDBACK, INIT_ESTIMATIONS = {}, {}
for a in ACTIONS:
    FEEDBACK[a] = a#''.join(rand.choice(string.ascii_lowercase) for _ in range(3))
    INIT_ESTIMATIONS[a] = None

if __name__ == "__main__":
    a = agent.Agent()
    print('action'.ljust(8) + 'estimated'.ljust(11) + 'real'.ljust(6) + 'state'.ljust(5))
    while True:
        action, estimated_feedback = a.get_next_action()
        a.give_real_feedback(FEEDBACK[action])
        print(str(action).ljust(8) + str(estimated_feedback).ljust(11) + str(FEEDBACK[action]).ljust(6) + str(a.get_etat()).ljust(5))
        sys.stdout.flush()
        time.sleep(.5)
