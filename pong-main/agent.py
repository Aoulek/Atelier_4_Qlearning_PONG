import numpy as np

class Qlearning:

    def __init__(self, screen_height, bar_height, alpha, gamma):
        # Initialisation des paramètres de l'agent
        self.alpha = alpha
        self.gamma = gamma
        self.Q = np.zeros([int(screen_height/bar_height), 2])
        self.rewards = []
        self.state = int((screen_height/bar_height) / 2)
        self.action = 0

    def get_action(self, s):
        # Retourne l'action avec la plus grande valeur Q pour l'état s
        return np.argmax(self.Q[s, :])

    def calculate_reward(rect, bar, ball):
        # Calcule la récompense pour une action en fonction de la position de la balle
        if bar.top <= ball.centery <= bar.bottom:
            return 1
        else:
            return -1

    def centre_to_state(self, centre, screen_height, bar_height):
        # Convertit la position verticale de la balle en état
        a = 0
        b = bar_height
        s = 0
        for i in range(int(screen_height/bar_height)):
            if a < centre < b:
                s = (b / bar_height) - 1
            else:
                a += bar_height
                b += bar_height
        return int(s)

    def update(self, s, bar, ball, screen_height, ball_speed_x, is_permanent):
        # Met à jour la valeur Q pour un état et une action donnés
        s_ = s
        position_cal = bar.right+10
        speed = ball_speed_x*(-1)
        ballX = ball.x
        if not is_permanent:
            position_cal = bar.left - 10 - ball.width
            speed = ball_speed_x
            ballX = position_cal
            position_cal = ball.x
        if position_cal <= ballX and speed > 0:
            reward = self.calculate_reward(bar, ball)
            self.rewards.append(reward)
            self.action = self.get_action(s)
            if self.action != 0:
                s_ = self.centre_to_state(ball.centery, screen_height, bar.height)
            else:
                s_ = s
            if s_ < 0:
                s_ = 0
            elif s_ > int(screen_height/bar.height)-1:
                s_ = int(screen_height/bar.height)-1
            self.state = s_
            self.Q[s, self.action] += self.alpha * (reward + self.gamma * np.max(self.Q[s_, :]) - self.Q[s, self.action])
        return s_ * bar.height
