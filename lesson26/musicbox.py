import playsound
import random
class Muzicbox():
    def __init__(self, ):
        self.variants = 'ABCDGIKNORTSUVXYZ'
        self.score = 1
        self.seqence = random.choice(self.variants)

    def __next(self):
        self.seqence += random.choice(self.variants)

    def check(self, user):
        if user == self.seqence:
            self.score += 1
            self.__next()
            playsound.playsound('zvuki\correct.wav')
        else:
            self.score -= 0.5
            playsound.playsound('zvuki\incorrect.wav')
    def play(self):
        for i in self.seqence:
            playsound.playsound(f'zvuki\{i}.mp3')