import game as g
import matplotlib.pyplot as plt
import numpy as np

def plot_agent_reward(rewards):
    """ Trace le cumul des récompenses de l'agent en fonction de l'épisode """
    plt.plot(np.cumsum(rewards))
    plt.title("Récompense cumulée de l'agent en fonction de l'épisode")
    plt.ylabel('Récompense')
    plt.xlabel('Épisode')
    plt.show()

class GameLearning:
    def __init__(self):
        while True:
            print('\n--- Choisissez un mode: --- ')
            mode = input('1. AgentRL vs AgentAI \n2. AgentRL vs Humain \n3. AgentRL vs AgentRL\nMode nº = ')
            if mode in {'1', '2', '3'}:
                break
        if mode == '1':
            self.game = g.Game('agentAI')
        elif mode == '2':
            self.game = g.Game('human')
        else:
            self.game = g.Game('agentRL')

    def beginPlaying(self):
        self.game.play()

if __name__ == '__main__':
    gl = GameLearning()
    gl.beginPlaying()
