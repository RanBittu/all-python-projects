"""
Created on:         05-aug-2023
@Author:            Ranjeet Kumar
Module Name:        appointment.py
"""
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from PyQt5.uic import loadUiType
import sys
import sqlite3
from datetime import date

ui, _ = loadUiType("login.ui")

"""
Application main class defined as:
MainApp
## In this missing Virtual Environment (venv)
"""
class MainApp(QMainWindow, ui):
  def __init__(self):
    QMainWindow.__init__(self)
    self.setupUi(self)
    self.tabWidget.setCurrentIndex(0)
    self.LOGINBUTTON.clicked.connect(self.login)
    self.LogoutIcon1.clicked.connect(self.logout)
    self.LogoutIcon2.clicked.connect(self.logout)
    self.LogoutIcon3.clicked.connect(self.logout)
    self.BookAppointmentIcon2.clicked.connect(self.show_book_appointment)
    self.BookAppointmentIcon3.clicked.connect(self.show_book_appointment)
    self.ConsultDoctorIcon1.clicked.connect(self.show_edit_appointment)
    self.ConsultDoctorIcon3.clicked.connect(self.show_edit_appointment)
    self.ReportsIcon1.clicked.connect(self.show_reports)
    self.ReportsIcon2.clicked.connect(self.show_reports)

  def login(self):
    """
    This code block defines a login method. 
    The method serves to handle the logic for a login process, 
    checking if the entered password matches a pre-defined value of "admin".

    The method takes self as an argument, 
    which refers to the instance of the object that is calling the method.

    The password entered by the user is retrieved from the PASSWORD 
    object using the text() method and stored in the "pw" variable.

    Conditional statement is used to check if the entered 
    password matches the value of "admin" (hard-coded value).

    If the entered password matches "admin", the following actions take place:

    The PASSWORD object's text is cleared using the setText("") method.
    The text in the LOGININFO object is cleared using the setText("") method.
    The current tab in the tabWidget object is set to the 
    first tab (index 1) using the setCurrentIndex(1) method.
    """
    pw = self.PASSWORD.text()
    if (pw == "admin"):
      self.PASSWORD.setText("")
      self.LOGININFO.setText("")
      self.tabWidget.setCurrentIndex(1)
    else:
      self.LOGININFO.setText("Invalid Password...!!")

  # below method is used for
  # Admin Logout functionality
  def logout(self):
      self.tabWidget.setCurrentIndex(0)

  # show book appointment tabfunction
  def show_book_appointment(self):
      self.tabWidget.setCurrentIndex(1)

  # show edit appointment tabfunction
  def show_edit_appointment(self):
      self.tabWidget.setCurrentIndex(2)

  # show reports tabfunction
  def show_reports(self):
      self.tabWidget.setCurrentIndex(3)

def main():
  app = QApplication(sys.argv)
  window = MainApp()
  window.show()
  app.exec_()

if __name__ == "__main__":
  main()
