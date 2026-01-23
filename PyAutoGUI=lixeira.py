import pyautogui
import time

pyautogui.hotkey('winleft', 'd') 

# Abre a lixeira
pyautogui.doubleClick(50, 50) # Coordenada aproximada da lixeira
time.sleep(1)

pyautogui.hotkey('ctrl', 'a') 
time.sleep(1)

# pyautogui.press('delete')
# time.sleep(1)
# pyautogui.press('enter')
pyautogui.hotkey('shift', 'delete')
time.sleep(3)

pyautogui.hotkey('n')