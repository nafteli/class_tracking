
import sys
import os
path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(f'{path}/gui')
sys.path.append(f'{path}/gui/students')
from gui.main_window import MainWindow


def main():
    MainWindow().run_main_window()

if __name__ == '__main__':
    main()