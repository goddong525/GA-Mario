#02.create-env.py
# 게임 환경 생성
import retro

env = retro.make(game = 'SuperMarioBros-Nes', state='Level1-1')
env.reset()

screen  = env.get_screen()


print(env)








