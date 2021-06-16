
import pyautogui
import mymodule1
import pyperclip

a = mymodule1.user2["user"]
b = mymodule1.user2["contactnumber"]
c = mymodule1.user2["desklocation"]
d = mymodule1.user2["username"]


#click cherwell
pyautogui.click(x=320, y=1056)
pyautogui.PAUSE = 2

#click my que
pyautogui.click(x=1102, y=469)
pyautogui.PAUSE = 2

# create new ticket
pyautogui.hotkey('ctrl', 'shift', 'i')

# type requestor
pyautogui.write((a), interval=0.1)
# tab through affected user
pyautogui.press(['tab','tab'])

#click short desription
pyautogui.click(x=559, y=284)

#type short description
pyautogui.write('Need Hardware | Wyse Terminal', interval=0.05)

#click description field
pyautogui.click(x=561, y=402)

#type description
pyautogui.write((d) + ' needs a Wyse terminal set up at desk location ' + (c) + '\n\nContact:\n' + (d) + (b))

#click contact method
pyautogui.click(x=818, y=525)

#press down twice for email or 5 for walk in
pyautogui.press(['down','down','enter'])

#click keyword classify
pyautogui.click(x=871, y=279)

#type reclaim
pyautogui.write('wyse', interval=0.05)

#press tab enter enter
pyautogui.press(['tab', 'enter', 'down', 'down', 'enter'])

#click activity
pyautogui.click(x=1131, y=284)

#write activity
pyautogui.write('Thank You!! ')

#click save
pyautogui.click(x=209, y=61)
pyautogui.PAUSE = 2

#click assign to team
pyautogui.click(x=1116, y=446)

#type reclaim
pyautogui.write('EUC team')

#press tab enter enter
pyautogui.press(['tab', 'enter', 'enter'])

pyperclip.copy('Service Request:\n' + d + ' - ' + c + '- Needs hardware - Wyse Terminal\n' + d + ': ' + b)

print('Service Request: ')
print((d), ' - ', (c), '- Needs hardware - Wyse Terminal')
print((d), ':', (b))
