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
        self._current_action = 0
        self._bored = False
        self._predilection_mem = [None] * (env.N_ACTIONS)
        print('action'.ljust(8) + 'anticipated'.ljust(13) + 'real'.ljust(6) + 'anticipation'.ljust(14) + 'predilection'.ljust(14) + 'excitation'.ljust(12))


    def live(self):
        anticipation = True
        predilection = True
        excitation = True

        self.get_next_action()
        self._state = (self._current_action, env.FEEDBACKS[self._current_action])
        self.update_boredom()

        a = self._current_action + 1
        an = self._predictions[self._current_action]
        r = env.FEEDBACKS[self._current_action]

        #anticipation
        if self._predictions[self._current_action] != env.FEEDBACKS[self._current_action]:
            anticipation = False
            self._predictions[self._current_action] = env.FEEDBACKS[self._current_action]

        #predilection
        if env.FEEDBACK_MATRIX[self._current_action]<0:
            predilection = False
            self._predilection_mem[self._current_action] = False
        else:
            self._predilection_mem[self._current_action] = True

        #excitation
        if self._bored:
            excitation = False

        ane = ':-)' if anticipation else ':-('
        pe = ':-)' if predilection else ':-('
        e = ':-)' if excitation else ':-('

        print(str(a).ljust(8) + str(an).ljust(13) + str(r).ljust(6) + ane.ljust(14) + pe.ljust(14) + e.ljust(12))


    def get_next_action(self):
        if self._bored:
            ca = self._current_action
            self._current_action = random.choice(list(range(0, ca))+ list(range(ca + 1, env.N_ACTIONS)))
            while self._predilection_mem[self._current_action] == False:
                self._current_action = random.choice(list(range(0, ca))+ list(range(ca + 1, env.N_ACTIONS)))
            self._bored = False

        return self._current_action

    def update_boredom(self):
        self._action_memory.append(self._current_action)
        self._action_memory.pop(0)
        
        if self._action_memory.count(self._current_action) >= self._boredom:
            self._bored = True



    # def get_etat(self):
    #     return m.STATES[self._state] if self._state != None else 'not set'
