from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from random import randint, shuffle 

class pertanyaan():
    def __init__(self, quest, jawaban_benar, opt1, opt2, opt3):
        self.quest = quest
        self.jawaban_benar = jawaban_benar
        self.opt1 = opt1
        self.opt2 = opt2
        self.opt3 = opt3

app = QApplication([])
btn = QPushButton('Cek Bro')
btngroup = QGroupBox('Pilihan ganda:')
btn1= QRadioButton('opt1')
btn2= QRadioButton('opt2')
btn3= QRadioButton('opt3')
btn4= QRadioButton('opt4')
btncontrolgroup = QButtonGroup()
btncontrolgroup.addButton(btn1)
btncontrolgroup.addButton(btn2)
btncontrolgroup.addButton(btn3)
btncontrolgroup.addButton(btn4)

quest_text = QLabel('text pertanyaan')
layout_pertanyaan = QHBoxLayout()
layout_pil_ganda1 = QVBoxLayout()
layout_pil_ganda2 = QVBoxLayout()
layout_pil_ganda1.addWidget(btn1)
layout_pil_ganda1.addWidget(btn2)
layout_pil_ganda2.addWidget(btn3)
layout_pil_ganda2.addWidget(btn4)
layout_pertanyaan.addLayout(layout_pil_ganda1)
layout_pertanyaan.addLayout(layout_pil_ganda2)
btngroup.setLayout(layout_pertanyaan)

ansgroupbox = QGroupBox('test results')
lb_correct = QLabel('bener g ni')
lb_answer = QLabel('Siap2 jawabannya adalah..')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_correct, alignment =(Qt.AlignLeft | Qt.AlignCenter))
layout_res.addWidget(lb_answer, alignment = Qt.AlignCenter)

ansgroupbox.setLayout(layout_res)

quest_layout = QHBoxLayout()
ans_layout = QHBoxLayout()
btn_layout = QHBoxLayout()

quest_layout.addWidget(quest_text, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
ans_layout.addWidget(btngroup)
ans_layout.addWidget(ansgroupbox)
btn_layout.addStretch(2)
btn_layout.addWidget(btn, alignment=Qt.AlignCenter, stretch=2)
btn_layout.addStretch(2)
main_layout = QVBoxLayout()
main_layout.addLayout(quest_layout, stretch=2)

main_layout.addLayout(ans_layout, stretch=8)
main_layout.addStretch(2)
main_layout.addLayout(btn_layout, stretch=3)
main_layout.addStretch(2)

main_layout.addSpacing(5)

def answer():
    btngroup.hide()
    ansgroupbox.show()
    btn.setText('Lanjut')

def show_quest():
    ansgroupbox.hide()
    btngroup.show()
    btn.setText('Cek Bro')
    btncontrolgroup.setExclusive(False)
    btn1.setChecked(False)
    btn2.setChecked(False)
    btn3.setChecked(False)
    btn4.setChecked(False)
    btncontrolgroup.setExclusive(True)
    
list_btn = [btn1,btn2,btn3,btn4]
def ask(q: pertanyaan):
    shuffle(list_btn)
    list_btn[0].setText(q.jawaban_benar)
    list_btn[1].setText(q.opt1)
    list_btn[2].setText(q.opt2)
    list_btn[3].setText(q.opt3)
    quest_text.setText(q.quest)
    lb_answer.setText(q.jawaban_benar)
    show_quest()

def show_correct(res):
    lb_correct.setText(res)
    answer()

def check_ans():
    if list_btn[0].isChecked():
        show_correct('Good')
        window.score += 1
        print('=== STATISTIC ===')
        print('Total quest: ' ,window.total)
        print('Total score: ', window.score)
        print('Rating: ', (window.score/window.total*100), '%')
    else:
        if list_btn[1].isChecked() or list_btn[2].isChecked() or list_btn[3].isChecked():
            show_correct('Nuh uh')
            print('Rating: ', (window.score/window.total*100), '%')

def next_quest():
    window.total+=1
    quest_now = randint(0,len(list_quest)-1)
    q = list_quest[quest_now]
    ask(q)

def check_btn():
    if btn.text() == 'Cek Bro':
        check_ans()
    else: 
        next_quest()

window = QWidget()
window.resize(500,500)
window.setLayout(main_layout)
window.setWindowTitle('Quiz App')

btn.clicked.connect(check_btn)
window.total = 0
window.score = 0

list_quest = []
list_quest.append(pertanyaan('Berimana kepada kitab Allah adalah rukum iman ke','3','1','2','4'))
list_quest.append(pertanyaan('Rasul dalam bahasa artinya adalah','Utusan','Yang dipercaya','Pembawa berita','Au'))
list_quest.append(pertanyaan('Nabi yang dapat gelar ulul azmi ada','5','2','1','6'))
list_quest.append(pertanyaan('Taurat berisi tentang','Hukum','Doa','Pujaan','Larangan'))
list_quest.append(pertanyaan('Surat an nas memiliki arti','Manusia','Jin','Azab','Semua benar'))
list_quest.append(pertanyaan('Posisi imam bila jenazah yang di sholatkan adalah laki adalah di','Kepala','Perut','Kaki','Paha'))

next_quest()

window.show()
app.exec()






