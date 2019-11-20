import random
import main as m
import environment as env
import time

# Trace de la forme : [(action,feedback reçu), (1, 0, 0)] où le second tuple correspond aux reward de estimation, prédilection, excitation
class Agent:
    def __init__(self):
        self._memory =  {}
        self._last_state = (0,0) #tuple (action,feedback)
        self._state = (0,0) #tuple (action,feedback)
        self._current_action = None



    #{last_state : {(a,f) : v}}

    def live(self):

        self._last_state = self._state
        if not (self._last_state in self._memory):
            self._memory[self._last_state]={}

        self.get_next_action()

        if (self._last_state[0] == self._current_action):
            self._state = (self._current_action, 1) #chosen feedback is 1
        else:
            self._state = (self._current_action, 2) #chosen feedback is 2

        if self._last_state!= (0,0):
            self.update_memory()


        print("state : "        +str(self._state), end=" | ")
        print("previous_state : " +str(self._last_state), end=" | ")
        if self._last_state!= (0,0):
            print("valence : "   +str(self._memory[self._last_state][self._state]))
        else:
            print("valence : _")
             


    def get_next_action(self):

        if self._memory == {}:
            self._current_action = random.choice(list(range(0, env.N_ACTIONS)))

        else:
            if self._memory[self._last_state] == {}:
                self._current_action = random.choice(list(range(0, env.N_ACTIONS)))
            else:
                tmp_key = max(self._memory[self._last_state],key= lambda x : self._memory[self._last_state][x])
                tmp_val = self._memory[self._last_state][tmp_key]

                if tmp_val < 0: #if the value is not acceptable (< 0)
                    if len(self._memory[self._last_state]) != env.N_ACTIONS*(len(env.F)-1): #if there's still unknown interactions
                        #find new iteractions

                        for a in range(0, env.N_ACTIONS):
                            for f in range(1, len(env.F)-1):
                                if not((a,f) in self._memory[self._last_state]):
                                    self._current_action=a
                                    return self._current_action

                    else:
                        self._current_action = random.choice(list(range(0, env.N_ACTIONS))) #random


                else:   #if the value is acceptable (>= 0)  
                    self._current_action = tmp_key[0]

        return self._current_action

    def update_memory(self):
        self._memory[self._last_state][self._state] = env.F[self._state[1]][self._state[0]]
