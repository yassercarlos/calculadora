import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi


class CalculatorWindow(QMainWindow):
    def __init__(self):
        super(CalculatorWindow, self).__init__()
        loadUi("calculadora.ui", self)
        
        self.frame.mouseMoveEvent = self.moveWindow      
   
        self.botones_numericos = [self.boton_0, self.boton_01, self.boton_02, self.boton_03, self.boton_04,
                                  self.boton_05, self.boton_06, self.boton_07, self.boton_08, self.boton_09]

        self.botones_operadores = [self.boton_sumar, self.boton_restar, self.boton_multiplicar, self.boton_dividir]

        self.boton_igual.clicked.connect(self.igual)
        self.boton_clean.clicked.connect(self.onac)
        self.boton_minimizar.clicked.connect(self.minimizar)
        self.boton_cerrar.clicked.connect(self.cerrar)

        for boton in self.botones_numericos:
            boton.clicked.connect(lambda checked, b=boton: self.agregar_texto(b.text()))

        for boton in self.botones_operadores:
            boton.clicked.connect(lambda checked, b=boton: self.agregar_texto(" " + b.text() + " "))
        
    def agregar_texto(self, texto):
        prev_text = self.label_prev.text()
        self.label_prev.setText(prev_text + texto)
        
    def minimizar(self):
        widget.showMinimized()       
         
    def igual(self):
        ecuacion = self.label_prev.text()
        try:
            ans =eval(ecuacion) 
            self.label_result.setText(str(ans))
        except:
            self.label_result.setText("")

    def onac(self):
        self.label_prev.setText("")
        self.label_result.setText("")
    
    def cerrar(self):
        app.exit()
        sys.exit()
    
    def moveWindow(self, e):
        if e.buttons() == Qt.LeftButton:
            self.move(self.pos()+ e.globalPos() - self.clickPosition)
            self.clickPosition = e.globalPos()
            e.accept()
            
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()
            
           
       
       
app = QApplication(sys.argv)
welcome = CalculatorWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)    
widget.setFixedHeight(1920)
widget.setFixedWidth(1080)
widget.setWindowFlags(QtCore.Qt.FramelessWindowHint)  
widget.setAttribute(QtCore.Qt.WA_TranslucentBackground)   
widget.show()
try:
    sys.exit(app.exec_()) 
except: 
    print("saliendo")
    

