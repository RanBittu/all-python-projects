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

  # below method is used for
  # Admin Login functionality
  def login(self):
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
