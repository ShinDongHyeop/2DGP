from pico2d import *

class Score:
    score = 0.0
    score_sound = None

    def stage1_score(self):
        Score.score += 1

    def stage2_score(self):
        Score.score += 2

    def stage3_score(self):
        Score.score += 2

    def stage4_score(self):
        Score.score += 3