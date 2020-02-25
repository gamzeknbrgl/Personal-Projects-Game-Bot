from PyQt5 import QtWidgets, uic, QtGui, QtCore
import pytesseract
import webbrowser
import pyautogui
import numpy
import cv2
import mss
import sys

class AnaEkran:
    def eliminate_option_a(self): # A şıkkını ele
        self.win.eliminate_option_a.setEnabled(False)
        self.win.eliminate_option_b.setEnabled(True)
        self.win.eliminate_option_c.setEnabled(True)
        self.win.search_text_option_a.setEnabled(False)
        self.win.search_text_option_b.setEnabled(True)
        self.win.search_text_option_c.setEnabled(True)
        self.win.answer_option_a.setEnabled(False)
        self.win.answer_option_b.setEnabled(True)
        self.win.answer_option_c.setEnabled(True)
        self.win.bc_click_button.setEnabled(True)
        self.win.ac_click_button.setEnabled(False)
        self.win.ab_click_button.setEnabled(False)
        self.win.search_image_option_a.setEnabled(False)
        self.win.search_image_option_b.setEnabled(True)
        self.win.search_image_option_c.setEnabled(True)
        self.win.bc_joker_button.setEnabled(True)
        self.win.ac_joker_button.setEnabled(False)
        self.win.ab_joker_button.setEnabled(False)
        self.disabled.append(0)

    def eliminate_option_b(self): # B şıkkını ele
        self.win.eliminate_option_a.setEnabled(True)
        self.win.eliminate_option_b.setEnabled(False)
        self.win.eliminate_option_c.setEnabled(True)
        self.win.search_text_option_a.setEnabled(True)
        self.win.search_text_option_b.setEnabled(False)
        self.win.search_text_option_c.setEnabled(True)
        self.win.answer_option_a.setEnabled(True)
        self.win.answer_option_b.setEnabled(False)
        self.win.answer_option_c.setEnabled(True)
        self.win.bc_click_button.setEnabled(False)
        self.win.ac_click_button.setEnabled(True)
        self.win.ab_click_button.setEnabled(False)
        self.win.search_image_option_a.setEnabled(True)
        self.win.search_image_option_b.setEnabled(False)
        self.win.search_image_option_c.setEnabled(True)
        self.win.bc_joker_button.setEnabled(False)
        self.win.ac_joker_button.setEnabled(True)
        self.win.ab_joker_button.setEnabled(False)
        self.disabled.append(1)

    def eliminate_option_c(self): # C şıkkını ele
        self.win.eliminate_option_a.setEnabled(True)
        self.win.eliminate_option_b.setEnabled(True)
        self.win.eliminate_option_c.setEnabled(False)
        self.win.search_text_option_a.setEnabled(True)
        self.win.search_text_option_b.setEnabled(True)
        self.win.search_text_option_c.setEnabled(False)
        self.win.answer_option_a.setEnabled(True)
        self.win.answer_option_b.setEnabled(True)
        self.win.answer_option_c.setEnabled(False)
        self.win.bc_click_button.setEnabled(False)
        self.win.ac_click_button.setEnabled(False)
        self.win.ab_click_button.setEnabled(True)
        self.win.search_image_option_a.setEnabled(True)
        self.win.search_image_option_b.setEnabled(True)
        self.win.search_image_option_c.setEnabled(False)
        self.win.bc_joker_button.setEnabled(False)
        self.win.ac_joker_button.setEnabled(False)
        self.win.ab_joker_button.setEnabled(True)
        self.disabled.append(2)

    def reset(self):
        self.win.eliminate_option_a.setEnabled(True)
        self.win.eliminate_option_b.setEnabled(True)
        self.win.eliminate_option_c.setEnabled(True)
        self.win.search_text_option_a.setEnabled(True)
        self.win.search_text_option_b.setEnabled(True)
        self.win.search_text_option_c.setEnabled(True)
        self.win.answer_option_a.setEnabled(True)
        self.win.answer_option_b.setEnabled(True)
        self.win.answer_option_c.setEnabled(True)
        self.win.bc_click_button.setEnabled(True)
        self.win.ac_click_button.setEnabled(True)
        self.win.ab_click_button.setEnabled(True)
        self.win.search_image_option_a.setEnabled(True)
        self.win.search_image_option_b.setEnabled(True)
        self.win.search_image_option_c.setEnabled(True)
        self.win.bc_joker_button.setEnabled(True)
        self.win.ac_joker_button.setEnabled(True)
        self.win.ab_joker_button.setEnabled(True)
        self.disabled = []

    def search_text_question(self):
        question = self.grab_ocr(self.monitor[0])
        question = self.ocr_to_que(question)
        url = "https://www.google.com.tr/search?q=" + question
        webbrowser.open(url, new=0, autoraise=True)

    def search_text_option_a(self):
        options = t.get_answers()
        url = "https://www.google.com.tr/search?q=" + options[0]
        webbrowser.open(url, new=0, autoraise=True)

    def search_text_option_b(self):
        options = t.get_answers()
        url = "https://www.google.com.tr/search?q=" + options[1]
        webbrowser.open(url, new=0, autoraise=True)

    def search_text_option_c(self):
        options = t.get_answers()
        url = "https://www.google.com.tr/search?q=" + options[2]
        webbrowser.open(url, new=0, autoraise=True)

    def search_text_all_options(self):
        options = t.get_answers()
        for i, text in enumerate(options):
            if i not in self.disabled:
                url = "https://www.google.com.tr/search?q={0}".format(options[i])
                webbrowser.open(url, new=0, autoraise=True)

    def search_image_option_a(self):
        options = t.get_answers()
        url = "https://www.google.com/search?q={0}&source=lnms&tbm=isch".format(options[0])
        webbrowser.open(url, new=0, autoraise=True)

    def search_image_option_b(self):
        options = t.get_answers()
        url = "https://www.google.com/search?q={0}&source=lnms&tbm=isch".format(options[1])
        webbrowser.open(url, new=0, autoraise=True)

    def search_image_option_c(self):
        options = t.get_answers()
        url = "https://www.google.com/search?q={0}&source=lnms&tbm=isch".format(options[2])
        webbrowser.open(url, new=0, autoraise=True)

    def search_image_option_all(self):
        options = t.get_answers()
        for i, text in enumerate(options):
            if i not in self.disabled:
                url = "https://www.google.com/search?q={0}&source=lnms&tbm=isch".format(options[i])
                webbrowser.open(url, new=0, autoraise=True)

    def click(self, option):
        for x, y in self.tdict[option]:
            pyautogui.click(x=x, y=y, interval=1)

    def clickk(self, option):
        for x, y in self.tdict2[option]:
            pyautogui.click(x=x, y=y, interval=1)

    def answer_option_a(self):
        t.click('a')

    def answer_option_b(self):
        t.click('b')

    def answer_option_c(self):
        t.click('c')

    def ab_click_button(self):
        t.click('d')

    def bc_click_button(self):
        t.click('e')

    def ac_click_button(self):
        t.click('f')

    def ab_joker_button(self): #
        t.click('j')
        t.click('a')
        t.click('b')

    def bc_joker_button(self): #
        t.click('j')
        t.click('b')
        t.click('c')

    def ac_joker_button(self): #
        t.click('j')
        t.click('a')
        t.click('c')

    def yandex_button(self):
        url = "https://yandex.com.tr/gorsel/?from=morda_new"
        webbrowser.open(url, new=0, autoraise=True)

    def google_button(self):
        url = "https://www.google.com.tr/imghp?hl=tr&tab=wi&ogbl"
        webbrowser.open(url, new=0, autoraise=True)

    def tdk_button(self):
        url = "http://sozluk.gov.tr"
        webbrowser.open(url, new=0, autoraise=True)

    def nisanyan_button(self):
        url = "https://www.nisanyansozluk.com"
        webbrowser.open(url, new=0, autoraise=True)

    def etimoloji_button(self):
        url = "https://www.etimolojiturkce.com"
        webbrowser.open(url, new=0, autoraise=True)

    def boxoffice_button(self):
        url = "https://boxofficeturkiye.com/tumzaman/"
        webbrowser.open(url, new=0, autoraise=True)

    def grab_ocr(self, screen):
        with mss.mss() as sct:
            img = numpy.array(sct.grab(screen))
            config = '-l tur --oem 1 --psm 3'
            text = pytesseract.image_to_string(img, config=config)
            return text

    def ocr_to_que(self, question):
        lines = question.split()
        question = ''
        flag = False
        for line in lines:
            if not flag:
                question = question + ' ' + line
            if '?' in line:
                flag = True
        return question

    def ocr_to_answer(self, options):
        options = options.strip()
        return options

    def get_answers(self):
        options = [self.grab_ocr(self.monitor[1])]
        options[0] = self.ocr_to_answer(options[0])
        options.append(self.grab_ocr(self.monitor[2]))
        options[1] = self.ocr_to_answer(options[1])
        options.append(self.grab_ocr(self.monitor[3]))
        options[2] = self.ocr_to_answer(options[2])
        return options

    def search_text_question_2(self):
        question = self.grab_ocr(self.monitor[4])
        question = self.ocr_to_que(question)
        url = "https://www.google.com.tr/search?q=" + question
        webbrowser.open(url, new=0, autoraise=True)

    def answer_correct(self):
        t.clickk('a2')

    def answer_wrong(self):
        t.clickk('b2')

    def joker_1_button(self):
        t.clickk('c2')

    def joker_2_button(self):
        t.clickk('d2')

    def cross_button(self):
        t.clickk('e2')

    def __init__(self):
        self.app = QtWidgets.QApplication([])
        self.win = uic.loadUi("ok.ui")
        # oyna kazan koordinatları buraya
        self.tdict = {
        'a': [(228, 270), (608, 257)],  # EMU 1,2 option A center
        'b': [(228, 316), (608, 293)],  # EMU 1,2 option B center
        'c': [(228, 362), (608, 331)],  # EMU 1,2 option C center

        'd': [(228, 270), (608, 293)],  # EMU 1 a, 2 b joker
        'e': [(228, 316), (608, 331)],  # EMU 1 b, 2 c joker
        'f': [(228, 270), (608, 331)],  # EMU 1 a, 2 c joker

        'j': [(167, 419), (546, 377)],  # EMU 1,2 joker center
        }
        self.monitor = [
        {"left": 68, "top": 202, "width": 318, "height": 47},  # ok question box coord
        {"left": 84, "top": 256, "width": 283, "height": 30},  # option a box coord
        {"left": 84, "top": 302, "width": 283, "height": 30},  # option b box coord
        {"left": 84, "top": 347, "width": 283, "height": 30},  # option c box coord
        {"left": 0, "top": 0, "width": 0, "height": 0}  # d-y question box coord
        ]
        # Doğru - yanlış koordinatları buraya
        self.tdict2 = {
        'a2': [(0, 0), (0, 0)],  # EMU 1,2 D center
        'b2': [(0, 0), (0, 0)],  # EMU 1,2 Y center
        'c2': [(0, 0), (0, 0)],  # EMU 1,2 joker 1 center
        'd2': [(0, 0), (0, 0)],  # EMU 1,2 joker 2 center
        'e2': [(0, 0), (0, 0)],  # EMU 1,2 çapraz işaretle
        }

        self.disabled = []
        self.win.eliminate_option_a.clicked.connect(self.eliminate_option_a)
        self.win.eliminate_option_b.clicked.connect(self.eliminate_option_b)
        self.win.eliminate_option_c.clicked.connect(self.eliminate_option_c)
        self.win.reset.clicked.connect(self.reset)
        self.win.search_text_option_a.clicked.connect(self.search_text_option_a)
        self.win.search_text_option_b.clicked.connect(self.search_text_option_b)
        self.win.search_text_option_c.clicked.connect(self.search_text_option_c)
        self.win.search_text_question.clicked.connect(self.search_text_question)
        self.win.search_text_all_options.clicked.connect(self.search_text_all_options)
        self.win.search_image_option_a.clicked.connect(self.search_image_option_a)
        self.win.search_image_option_b.clicked.connect(self.search_image_option_b)
        self.win.search_image_option_c.clicked.connect(self.search_image_option_c)
        self.win.search_image_option_all.clicked.connect(self.search_image_option_all)
        self.win.answer_option_a.clicked.connect(self.answer_option_a)
        self.win.answer_option_b.clicked.connect(self.answer_option_b)
        self.win.answer_option_c.clicked.connect(self.answer_option_c)
        self.win.bc_joker_button.clicked.connect(self.bc_joker_button)
        self.win.ac_joker_button.clicked.connect(self.ac_joker_button)
        self.win.ab_joker_button.clicked.connect(self.ab_joker_button)
        self.win.bc_click_button.clicked.connect(self.bc_click_button)
        self.win.ac_click_button.clicked.connect(self.ac_click_button)
        self.win.ab_click_button.clicked.connect(self.ab_click_button)
        self.win.yandex_button.clicked.connect(self.yandex_button)
        self.win.google_button.clicked.connect(self.google_button)
        self.win.tdk_button.clicked.connect(self.tdk_button)
        self.win.etimoloji_button.clicked.connect(self.etimoloji_button)
        self.win.nisanyan_button.clicked.connect(self.nisanyan_button)
        self.win.boxoffice_button.clicked.connect(self.boxoffice_button)
        self.win.search_text_question_2.clicked.connect(self.search_text_question_2)
        self.win.answer_correct.clicked.connect(self.answer_correct)
        self.win.answer_wrong.clicked.connect(self.answer_wrong)
        self.win.cross_button.clicked.connect(self.cross_button)
        self.win.joker_1_button.clicked.connect(self.joker_1_button)
        self.win.joker_2_button.clicked.connect(self.joker_2_button)
        self.win.show()

if __name__ == '__main__':
    t = AnaEkran()
    sys.exit(t.app.exec())
