#03. get_screen.py
# 게임 화면 가져오기
import sys
import retro

from PyQt5.QtWidgets import QLabel


#게임 환경 생성
env = retro.make(game = 'SuperMarioBros-Nes', state='Level1-1')
#새 게임 시작
env.reset()

#화면 가져오기
screen = env.get_screen()


print(screen.shape[0], screen.shape[1])
#print(screen)


