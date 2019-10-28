import agent
import random as rand
import string
import time
import sys

BORED_IN = 4
HAPPY, SAD, BORED = ':-)', ':-(', ':-Z'
STATES = [HAPPY, SAD, BORED]
ACTIONS = ['A', 'B', 'C', 'D', 'E']
FEEDBACK, INIT_ESTIMATIONS = {}, {}
for a in ACTIONS:
    FEEDBACK[a] = ''.join(rand.choice(string.ascii_lowercase) for _ in range(3))
    INIT_ESTIMATIONS[a] = None

if __name__ == "__main__":
    a = agent.Agent()
    while True:
        action, estimated_feedback = a.get_next_action()
        a.give_real_feedback(FEEDBACK[action])
        print('Action: ', action, ', estimated feedback: ', estimated_feedback,
        'real feedback: ', FEEDBACK[action], ', state: ', a.get_etat())
        sys.stdout.flush()
        time.sleep(.5)
