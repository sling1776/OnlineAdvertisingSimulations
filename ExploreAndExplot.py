import numpy as np
import matplotlib.pyplot as plt
np.random.seed(0)


class Environment:

    def __init__(self, probs):
        self.probs = probs  # success probabilities for each arm

    def step(self, action):
        # Pull arm and get stochastic reward (1 for success, 0 for failure)
        return self.probs[action]()
    

class Agent:

    def __init__(self, nActions, eps):
        self.nActions = nActions
        self.eps = eps
        self.n = np.zeros(nActions)#, dtype=np.int) # action counts n(a)
        self.Q = np.zeros(nActions)#, dtype=np.float) # value Q(a)

    def update_Q(self, action, reward):
        # Update Q action-value given (action, reward)
        self.n[action] += 1
        self.Q[action] += (1.0/self.n[action]) * (reward - self.Q[action])

    def get_action(self):
        # Epsilon-greedy policy
        if np.random.random() < self.eps: # explore
            return np.random.randint(self.nActions)
        else: # exploit
            return np.random.choice(np.flatnonzero(self.Q == self.Q.max()))


def get_probabilities():
    probs = [
        lambda : np.random.beta(7, 3) + 2,
        lambda : np.random.uniform(0, 4),
        lambda : np.random.beta(3, 7) + 2,
        lambda : np.random.normal(2, 1.4),
        lambda : np.random.normal(1.3, 7)
    ]
    return probs

# Start multi-armed bandit simulation
def experiment(probs, N_episodes, epsilon=.1, base=None):
    env = Environment(probs) # initialize arm probabilities
    agent = Agent(len(env.probs), epsilon)  # initialize agent
    actions, rewards = [], []
    for episode in range(N_episodes):
        action = agent.get_action() # sample policy
        reward = env.step(action) # take step + get reward
        if base:
            base = 0 if base < 0 else base
            reward = 0 if reward < base else reward
        agent.update_Q(action, reward) # update Q
        actions.append(action)
        rewards.append(reward)
    return np.array(actions), np.array(rewards)






NUM_DAYS = 500 # number of steps (episodes)
EPSILON = 0.1 # probability of random exploration (fraction)
NUM_SIMULATIONS = 10000

R = np.zeros((NUM_DAYS,))  # reward history sum
A = np.zeros((NUM_DAYS, len(get_probabilities())))  # action history sum

for i in range(NUM_SIMULATIONS):
    probs = get_probabilities()
    actions, rewards = experiment(probs, NUM_DAYS, EPSILON)  # perform experiment
    R += rewards
    for step, action in enumerate(actions):
        A[step][action] += 1

R_avg =  R / float(NUM_SIMULATIONS)
plt.plot(R_avg, ".")
plt.xlabel("Step")
plt.ylabel("Average Reward")
plt.grid()
plt.show()

for i in range(len(probs)):
    steps = list(np.array(range(len(A)))+1)
    plt.plot(steps, A[:, i], ".",
        linewidth=5,
        label="Arm {}".format(i+1))
plt.xlabel("Step")
plt.ylabel("Selection over Time")
plt.legend(loc='upper left', shadow=True)
plt.xlim([1, NUM_DAYS])
plt.ylim([0, NUM_SIMULATIONS])
plt.show()