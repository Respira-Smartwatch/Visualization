from PyQt5 import QtWidgets
import pyqtgraph as pg
from typing import Callable

class Graph_Layout(QtWidgets.QWidget):
    def __init__(self, 
                 file_button_method: Callable, 
                 graph_number: int=1,
                 button_width: int=75,
                 *args, **kwargs):

        super(Graph_Layout, self).__init__(*args, **kwargs)
        # Create required objects
        layout = QtWidgets.QVBoxLayout()
        bottom_bar_layout = QtWidgets.QHBoxLayout()   
        self.graph = pg.PlotWidget()
        self.label = QtWidgets.QLabel("None")

        # Setup for required objects
        self.file_button = QtWidgets.QPushButton("Browse")  
        self.file_button.setMaximumWidth(button_width)
        self.file_button.clicked.connect(file_button_method)

        self.graph_number = graph_number

        self.graph.setTitle(f"Graph {graph_number}", color="b", size='20pt')        
        self.graph.showGrid(x=True, y=True)

        #self.graph.setBackground("w")

        # Layout configuration
        bottom_bar_layout.addWidget(self.file_button)
        bottom_bar_layout.addWidget(self.label)

        layout.addWidget(self.graph)
        layout.addLayout(bottom_bar_layout)

        self.setLayout(layout)
    
    def set_title(self, title: str, color: str="b", size: str='20pt'):
        self.graph.setTitle(f"{title}", color=color, size=size)
    
class Audio_Graph_Layout(QtWidgets.QWidget):
    def __init__(self, 
                 file_button_method: Callable, 
                 play_button_method: Callable,
                 graph_number: int = 1, 
                 button_width: int = 75,
                 *args, **kwargs):

        super(Audio_Graph_Layout, self).__init__(*args, **kwargs)
        """ A method that creates an audio_graph graph view up to 10"""

         # Create required objects
        layout = QtWidgets.QVBoxLayout()
        self.bottom_bar_layout = QtWidgets.QHBoxLayout()   
        self.graph = pg.PlotWidget()
        self.label = QtWidgets.QLabel("None")

        # Setup for required objects
        self.file_button = QtWidgets.QPushButton("Browse")  
        self.file_button.setMaximumWidth(button_width)
        self.file_button.clicked.connect(file_button_method)
        self.playBtn = QtWidgets.QPushButton("Play")
        self.playBtn.setMaximumWidth(button_width)
        self.playBtn.clicked.connect(play_button_method)

        self.graph.setTitle(f"Audio Graph {graph_number}", color="b", size='20pt')        
        self.graph.showGrid(x=True, y=True)
        #g.setBackground("w")

        # Layout configuration
        self.bottom_bar_layout.addWidget(self.file_button)
        self.bottom_bar_layout.addWidget(self.label)
        self.bottom_bar_layout.addWidget(self.playBtn)

        self.graph_number = graph_number


        # Layout configuration
        layout.addWidget(self.graph)
        layout.addLayout(self.bottom_bar_layout)

        self.setLayout(layout)
    
    def set_title(self, title: str, color: str="b", size: str='20pt'):
        self.graph.setTitle(f"{title}", color=color, size=size)