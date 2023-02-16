import sys
import os


path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(f'{path}/gui')
sys.path.append(f'{path}/gui/students') 
sys.path.append(f'{path}/methode')
sys.path.append(f'{path}/tests/')
sys.path.append(f'{path}/tests/test_metode/')