import pyautogui
import time
import keyboard
def click():
	pyautogui.click(500, 500)
status = 0
print ('Press "q" to exit of the program, please!')
for i in range(1,10000):
	click()
	for i in range(1,1000):
		if keyboard.is_pressed('q'):  # if key 'q' is pressed 
				print('You Pressed A Key!')
				status = 1
				break  # finishing the loop
		time.sleep(0.01)
	if status == 1:
		break