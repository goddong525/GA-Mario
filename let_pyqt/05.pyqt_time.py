#05. pyqt_timer.py
#PyQt 타이머 예제


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtCore import QTimer
class MyApp(QWidget):
    # GUI 창 속에 띄울 요소 - QWidget을 베이스로하는 껍데기 만든 것
    # Class는 붕어빵과 붕어빵틀 중에 붕어빵틀에 해당이 됨
    def __init__(self):     #초기화자, 생성자 역할을 한다고 생각하면 됨
        super().__init__()  #C/C++에서 #include부터 return 0까지하는 거라고 보면 됨

        self.setFixedSize(400, 300) # 창 크기 고정, self는 나!

        self.setWindowTitle('My Window')    #창 제목

        self.show()         #창 띄우기

        #타이머 설정
        qtimer = QTimer(self)
        #타이머에 실행할 함수 연결
        qtimer.timeout.connect(self.timer)

        #1초(=1000밀리초)마다 연결된 함수를 실행
        qtimer.start(1000)

        # 텍스트 삽입하기
        label_text = QLabel(self)
        label_text.setText('timer')      #텍스트 이름 정하기
        label_text.setGeometry(0, 0, 400, 300)



#주기적으로 실행할 함수
    def timer(self):
        print('timer')

if __name__ == '__main__':   #여기에 적는 코드들은 직접 실행할 때만 실행가능, 외부에서 불러올 경우 여기에 포함된 코드는 실행되지 않음
    app = QApplication(sys.argv)
    window = MyApp()        # 붕어빵을 찍어내는 것, 붕어빵 이름이 window
    sys.exit(app.exec())    #여기까지 거의 고정적으로 쓰는 코드들들
