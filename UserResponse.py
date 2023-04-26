import numpy as np
import matplotlib.pyplot as plt
from ExploreAndExploit import experiment

def get_probabilities():

    facebook = [
        # Native ads
        lambda : np.random.normal(np.random.uniform(.33, .38)), # .33 - .38

        # Video ads
        lambda : np.random.normal(np.random.uniform(.5, .73)), # .5 - .73

        # Carousel ads
        lambda : np.random.normal(np.random.uniform(.3, .85)), # .3 - .85

        # Interactive ads
        lambda : np.random.normal(np.random.uniform(1.25, 1.33)), # 1.25 - 1.33

    ]

    google = [
        # Search ads
        lambda : np.random.normal(3.17), # 3.17

        # Display ads
        lambda : np.random.normal(.46), # .46
    ]

    email = [
        # Americas
        lambda : np.random.normal(2.2), # 2.2

        # UK
        lambda : np.random.normal(2.4), # 2.4

        # Europe
        lambda : np.random.normal(2.2), # 2.2

        # Asia/Pacific
        lambda : np.random.normal(3), # 3
    ]

    probs = facebook + google + email

    return probs

def main():
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

    names = ["FB Native", "FB Video", "FB Carousel", "FB Interactive", "Google Search", "Google Display", "Email America", "Email UK", "Email Europe", "Email Asia/Pacific"]

    for i in range(len(probs)):
        steps = list(np.array(range(len(A)))+1)
        plt.plot(steps, A[:, i], ".",
            linewidth=5,
            label=names[i])
    plt.xlabel("Step")
    plt.ylabel("Selection over Time")
    plt.legend(loc='upper left', shadow=True)
    plt.xlim([1, NUM_DAYS])
    plt.ylim([0, NUM_SIMULATIONS])
    plt.title("Using the Epsilong Greedy algorithm to decide on Advertisement strategy")
    plt.show()

if __name__ == "__main__":
    main()