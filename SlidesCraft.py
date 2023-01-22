#<==========IMPORTING MODULES==========>
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPixmap, QIcon, QFontDatabase
from themes import *
import threading
import sys
import time

#<===============CREATING A QWIDGET CLASS=====================>
class App(QWidget):
	def __init__(self):
		super().__init__()
		#SETTING THE PROPERTIES OF THE MAIN WINDOW
		self.setWindowTitle("SlidesCraft")
		self.setWindowIcon(QIcon("logo.png"))
		self.resize(1224, 771)
		self.setMaximumSize(1224, 771)
		self.setStyleSheet("background:rgb(30,30,20);")

		#Background
		self.bg = QtWidgets.QLabel(self)
		self.bg.setGeometry(QtCore.QRect(-100, 0, 1400, 771))
		pixmap = QPixmap("bg/1.png")
		self.bg_index = 1
		self.bg.setPixmap(pixmap)
		self.bg.setScaledContents(True)

		#Fonts Setup
		font_extra = QFontDatabase.addApplicationFont("fonts/Baby Doll.ttf")
		font_families = QFontDatabase.applicationFontFamilies(font_extra)
		font = QtGui.QFont(font_families[0])
		font.setPointSize(25)

		font2 = QtGui.QFont(font_families[0])
		font2.setPointSize(45)

		#Variable Declaration
		self.name = "Name"
		self.title = "Title"
		self.slidecount = 5
		self.templateno = 1

		#Input - TITLE
		self.input_title = QtWidgets.QLineEdit(self)
		self.input_title.setGeometry(QtCore.QRect(650, 240, 400, 100))
		self.input_title.setStyleSheet("background:transparent;border:0px;color:white;")
		self.input_title.setFont(font)
		self.input_title.setHidden(True)

		#Input - SLIDECOUNT
		self.input_slidecount = QtWidgets.QLineEdit(self)
		self.input_slidecount.setGeometry(QtCore.QRect(520, 350, 65, 100))
		self.input_slidecount.setStyleSheet("background:transparent;border:0px;color:black;")
		self.input_slidecount.setFont(font2)
		validator = QtGui.QIntValidator(1, 10)
		self.input_slidecount.setValidator(validator)
		self.input_slidecount.setHidden(True)

		#Input - NAME
		self.input_name = QtWidgets.QLineEdit(self)
		self.input_name.setGeometry(QtCore.QRect(650, 240, 400, 100))
		self.input_name.setStyleSheet("background:transparent;border:0px;color:white;")
		self.input_name.setFont(font)
		self.input_name.setHidden(True)

		#TEMPLATES - BUTTONS (1-4)
		self.template1 = QtWidgets.QPushButton(self)
		self.template1.setGeometry(QtCore.QRect(257, 244, 292, 160))
		self.template1.setStyleSheet("QPushButton{background:rgba(0, 255, 0,0.9);border:0px;border-radius:12px;color:black;}QPushButton::hover{background:rgba(120, 28, 176,0.8)}")
		self.template3 = QtWidgets.QPushButton(self)
		self.template3.setGeometry(QtCore.QRect(570, 244, 292, 160))
		self.template3.setStyleSheet("QPushButton{background:rgba(0,0,0,0.1);border:0px;border-radius:12px;color:black;}QPushButton::hover{background:rgba(0,255,0,0.8)}")
		self.template2 = QtWidgets.QPushButton(self)
		self.template2.setGeometry(QtCore.QRect(257, 244+185, 292, 160))
		self.template2.setStyleSheet("QPushButton{background:rgba(0,0,0,0.1);border:0px;border-radius:12px;color:black;}QPushButton::hover{background:rgba(0,255,0,0.8)}")
		self.template4 = QtWidgets.QPushButton(self)
		self.template4.setGeometry(QtCore.QRect(570, 244+185, 292, 160))
		self.template4.setStyleSheet("QPushButton{background:rgba(0,0,0,0.1);border:0px;border-radius:12px;color:black;}QPushButton::hover{background:rgba(0,255,0,0.8)}")
		self.template1.setHidden(True)
		self.template2.setHidden(True)
		self.template3.setHidden(True)
		self.template4.setHidden(True)


		#CONNECTIONS AND SLOTS
		self.template1.clicked.connect(lambda:click_template(selected=self.template1,number=1))
		self.template2.clicked.connect(lambda:click_template(selected=self.template2,number=2))
		self.template3.clicked.connect(lambda:click_template(selected=self.template3,number=3))
		self.template4.clicked.connect(lambda:click_template(selected=self.template4,number=4))

		# FUNCTION THAT CHANGES THE APPEARANCE OF SELECTED TEMPLATE BUTTON AND UPDATE THE TEMPLATE NO ID
		def click_template(selected,number):
			self.template1.setStyleSheet("QPushButton{background:rgba(0,0,0,0.1);border:0px;border-radius:12px;color:black;}QPushButton::hover{background:rgba(0,255,0,0.8)}")
			self.template2.setStyleSheet("QPushButton{background:rgba(0,0,0,0.1);border:0px;border-radius:12px;color:black;}QPushButton::hover{background:rgba(0,255,0,0.8)}")
			self.template3.setStyleSheet("QPushButton{background:rgba(0,0,0,0.1);border:0px;border-radius:12px;color:black;}QPushButton::hover{background:rgba(0,255,0,0.8)}")
			self.template4.setStyleSheet("QPushButton{background:rgba(0,0,0,0.1);border:0px;border-radius:12px;color:black;}QPushButton::hover{background:rgba(0,255,0,0.8)}")
			selected.setStyleSheet("QPushButton{background:rgba(0, 255, 0,0.9);border:0px;border-radius:12px;color:black;}QPushButton::hover{background:rgba(120, 28, 176,0.8)}")
			self.templateno = number


	#TO DETECT THE KEY PRESSED IN THE PROGRAM
	def keyPressEvent(self, event):
		#Updating Screen based on the "bg_index" var. Hiding/Showing the required elements and setting them to focus.
		def update_screen():
			#INTRODUCTION- SCREEN
			if self.bg_index == 1:
				self.input_name.setHidden(True)
				self.input_slidecount.setHidden(True)
				self.input_title.setHidden(True)
				self.template1.setHidden(True)
				self.template2.setHidden(True)
				self.template3.setHidden(True)
				self.template4.setHidden(True)

			#TITLE INPUT - SCREEN
			if self.bg_index == 2:
				self.input_name.setHidden(True)
				self.input_slidecount.setHidden(True)
				self.input_title.setHidden(False)
				self.template1.setHidden(True)
				self.template2.setHidden(True)
				self.template3.setHidden(True)
				self.template4.setHidden(True)
				self.input_title.setFocus()

			#SLIDE COUNT SELECTING - SCREEN
			elif self.bg_index == 3:
				self.input_name.setHidden(True)
				self.input_slidecount.setHidden(False)
				self.input_title.setHidden(True)
				self.template1.setHidden(True)
				self.template2.setHidden(True)
				self.template3.setHidden(True)
				self.template4.setHidden(True)
				self.input_slidecount.setFocus()

			#NAME INPUT - SCREEN
			elif self.bg_index == 4:
				self.input_name.setHidden(False)
				self.input_slidecount.setHidden(True)
				self.input_title.setHidden(True)
				self.template1.setHidden(True)
				self.template2.setHidden(True)
				self.template3.setHidden(True)
				self.template4.setHidden(True)
				self.input_name.setFocus()

			#SLIDES DESIGN - SCREEN
			elif self.bg_index == 5:
				self.input_name.setHidden(True)
				self.input_slidecount.setHidden(True)
				self.input_title.setHidden(True)
				self.template1.setHidden(False)
				self.template2.setHidden(False)
				self.template3.setHidden(False)
				self.template4.setHidden(False)

			#CREATING THE PPT - SCREEN
			elif self.bg_index == 6:
				#creating the emoji animation screen
				def loading_animation():
					while True:
						if self.bg_index!=6:
							self.bg_index = 1
							self.bg.setPixmap(QPixmap(f"bg/{self.bg_index}.png"))
							update_screen()
							self.input_title.setText("")
							self.input_name.setText("")
							self.input_slidecount.setText("")
							break
						else:
							self.bg.setPixmap(QPixmap(f"bg/6.png"))
							time.sleep(0.10)
							self.bg.setPixmap(QPixmap(f"bg/7.png"))
							time.sleep(0.10)
							self.bg.setPixmap(QPixmap(f"bg/8.png"))
							time.sleep(0.10)

				self.input_name.setHidden(True)
				self.input_slidecount.setHidden(True)
				self.input_title.setHidden(True)
				self.template1.setHidden(True)
				self.template2.setHidden(True)
				self.template3.setHidden(True)
				self.template4.setHidden(True)
				#Using thread to let the create_ppt function run parallaly without hanging the application 
				secondary_thread = threading.Thread(target=create_ppt)
				secondary_thread.start()
				third_thread = threading.Thread(target=loading_animation)
				third_thread.start()

		def create_ppt():
				self.title = self.input_title.text()
				self.name = self.input_name.text()

				#If you forget to enter any values, it will just rick roll you😵
				#I would have added an error dialogue box instead but got no time for that😭
				if self.slidecount == "":
					self.slidecount = 5

				if self.title == "":
					self.title = "Rick Roll"

				if self.name == "":

					self.name = "Rick Astley"

				#Creating the PPT from THEMES.py based on the template you have chosed)
				if self.templateno-1 == 0:
					create_ppt_2(self.title, self.name, self.slidecount)
				elif self.templateno-1 == 1:
					create_ppt_3(self.title, self.name, self.slidecount)
				elif self.templateno-1 == 2:
					create_ppt_4(self.title, self.name, self.slidecount)
				elif self.templateno-1 == 3:
					create_ppt_5(self.title, self.name, self.slidecount)

				#After the ppt is created the values are cleared and we are back to homescreen
				self.bg_index = 1
				self.bg.setPixmap(QPixmap(f"bg/{self.bg_index}.png"))
				update_screen()
				self.input_title.setText("")
				self.input_name.setText("")
				self.input_slidecount.setText("")

		#Changing the Background to next background on enter pressed
		if event.key() == QtCore.Qt.Key_Return:
			if self.bg_index!=6:
				self.bg_index += 1
				self.bg.setPixmap(QPixmap(f"bg/{self.bg_index}.png"))
				update_screen()

			else:
				print(">> End of Screen <<")
		# Changing the background to previous background on Escape Pressed
		if event.key() == QtCore.Qt.Key_Escape:
			if self.bg_index!=1 and self.bg_index!=6:
				self.bg_index -= 1
				self.bg.setPixmap(QPixmap(f"bg/{self.bg_index}.png"))
				update_screen()

if __name__=="__main__":
	#Creating the QApplication Class and adding connecting it to QWidget
	app = QApplication(sys.argv)
	a = App()
	a.show()
	sys.exit(app.exec_())



