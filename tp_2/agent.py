import random
import main as m
import environment as env
import time

# Trace de la forme : [(action,feedback reçu), (1, 0, 0)] où le second tuple correspond aux reward de estimation, prédilection, excitation
class Agent:
    def __init__(self):
        self._predictions = [None] * (env.N_ACTIONS)
        self._boredom = 3
        self._state = (0,0) #tuple (action,feedback)
        self._action_memory = [None] * self._boredom
        self._current_action = None
        self._bored = False


    def live(self):
        anticipation = True
        predilection = True
        excitation = True

        self.get_next_action()
        self._state = (self._current_action, env.FEEDBACKS[self._current_action])
        self.update_boredom()

        #anticipation
        if self._predictions[self._current_action] != env.FEEDBACKS[self._current_action]:
            anticipation = False
            self._predictions[self._current_action] = env.FEEDBACKS[self._current_action]

        #predilection
        if env.FEEDBACK_MATRIX[self._current_action]<0:
            predilection = False

        #excitation
        if self._bored:
            excitation = False

        print("state : "        +str(self._state), end=" | ")
        print("anticipation : " +str(anticipation), end=" | ")
        print("predilection : " +str(predilection), end=" | ")
        print("excitation : "   +str(excitation))


    def get_next_action(self):
        if self._bored:
            self._current_action = random.choice(list(range(0, self._current_action))+ list(range(self._current_action+1, env.N_ACTIONS)))
            self._bored = False
        else:
            self._current_action = random.choice(range(env.N_ACTIONS))

        return self._current_action

    def update_boredom(self):
        self._action_memory.append(self._current_action)
        self._action_memory.pop(0)
        
        if self._action_memory.count(self._current_action) >= self._boredom:
            self._bored = True



    # def get_etat(self):
    #     return m.STATES[self._state] if self._state != None else 'not set'
