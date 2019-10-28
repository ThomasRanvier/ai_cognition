import random
import main as m

class Agent:
    def __init__(self):
        self._predictions = {}
        self._state = m.STATES.index(m.BORED)
        self._state_memory = [None] * m.BORED_IN
        self._estimations = m.INIT_ESTIMATIONS
        self._current_action = None

    def get_next_action(self):
        if m.STATES[self._state] == m.BORED:
            actions = m.ACTIONS.copy()
            if self._current_action is not None:
                actions.remove(self._current_action)
            self._current_action = random.choice(actions)
        return self._current_action, self._estimations[self._current_action]

    def give_real_feedback(self, feedback):
        if self._estimations[self._current_action] == feedback:
            self._set_state(m.HAPPY)
        else:
            self._set_state(m.SAD)
            self._estimations[self._current_action] = feedback

    def _set_state(self, state):
        self._state = m.STATES.index(state)
        self._state_memory.append(self._state)
        self._state_memory.pop(0)
        if self._state_memory.count(m.STATES.index(m.HAPPY)) >= m.BORED_IN:
            self._set_state(m.BORED)


    def get_etat(self):
        return m.STATES[self._state] if self._state != None else 'not set'
