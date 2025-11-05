from PyQt6.QtWidgets import QApplication, QMainWindow


from HousePricePredictionEx import HousePricePredictionEx

app=QApplication([])
myWindow=HousePricePredictionEx()
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()