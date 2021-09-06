


pip install PyQtWebEngine


from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *  #QIcon
from PyQt5.QtWebEngineWidgets import *
import sys
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()
        # create instance of toolbar
        nav = QToolBar()
        # set icon size
        nav.setIconSize(QSize(24,24))
        # add toolbar on MainWindow
        self.addToolBar(nav)
        # create buttons on navigation toolbar
        home_btn = QAction(QIcon("home.png"),'Click to open Home page', self)
        home_btn.triggered.connect(self.home)
        nav.addAction(home_btn)
        back_btn = QAction(QIcon("backward.png"),'Click to go back', self)
        back_btn.triggered.connect(self.browser.back)
        nav.addAction(back_btn)
        forward_btn = QAction(QIcon("forward.png"),'Click to go forward', self)
        forward_btn.triggered.connect(self.browser.forward)
        nav.addAction(forward_btn)
        reload_btn = QAction(QIcon("refresh.png"),'Click to Refresh this page', self)
        reload_btn.triggered.connect(self.browser.reload)
        nav.addAction(reload_btn)
        # create entry widget to enter url
        self.url_entry = QLineEdit()
        self.url_entry.returnPressed.connect(self.navigate_to_url)
        nav.addWidget(self.url_entry)
        self.browser.urlChanged.connect(self.update_url)
    def home(self):
        # set home url
        self.browser.setUrl(QUrl('https://google.com'))
    def navigate_to_url(self):
        # get url
        url = self.url_entry.text()
        # set url
        self.browser.setUrl(QUrl(url))
    def update_url(self, entered_url):
        # update url to entry widget
        self.url_entry.setText(entered_url.toString())
app = QApplication(sys.argv)
QApplication.setApplicationName('Browser')
window = MainWindow()
app.exec_()






