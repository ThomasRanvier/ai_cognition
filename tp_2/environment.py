import main as m

F=[None, [1,1,-1], [1,-1,1]] #f0 does not exists
FEEDBACKS = [1,2,2] #env2: a1->f1, a2->f2, a3->f2
FEEDBACK_MATRIX = [F[FEEDBACKS[i]][i] for i in range(3)]  #the feedback matrix chosen by the environment (in this case, we have env2: a1->f1, a2->f2, a3->f2 ) 

N_ACTIONS = len(FEEDBACKS) # actions are numbers from 0 to N_ACTIONS-1 (There are 3 actions)
        