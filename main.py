
import sys
sys.path.append('/home/evyatar/PycharmProjects/class_tracking/gui')
sys.path.append('/home/evyatar/PycharmProjects/class_tracking/gui/students')
from gui.main_window import MainWindow


def main():
    MainWindow().run_main_window()

if __name__ == '__main__':
    main()