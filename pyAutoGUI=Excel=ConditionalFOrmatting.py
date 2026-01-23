import pyautogui
import time

#pyautogui.hotkey('winleft', 'd') 
#pyautogui.hotkey('winleft', 'r') 
pyautogui.hotkey('alt', 'tab') 
time.sleep(1)
# pyautogui.write('excel')
# time.sleep(1)
# pyautogui.press('enter')
#time.sleep(5)  # Aguarda o Excel abrir

#with pyautogui.hold('shift'):
pyautogui.press(['alt', 'c', 'l', 'r', 's'])

# pyautogui.write('Este documento foi criado automaticamente usando PyAutoGUI.', interval=0.02)
# time.sleep(1)
# pyautogui.hotkey('ctrl', 'b' ) # O Excel em português usa as teclas de atalho F12 ou CTRL+B  para salvar os arquivos ao invés de CTRL+S que usa na versão em inglês
# time.sleep(10)
# pyautogui.write('Documento_Automatico.xlsx')
# time.sleep(1)
# pyautogui.press('enter')
# time.sleep(2)
#pyautogui.hotkey('alt', 'l' )
# pyautogui.hotkey('alt', 'f4')
# time.sleep(1)
# pyautogui.press('n')  # Não salvar alterações se solicitado


