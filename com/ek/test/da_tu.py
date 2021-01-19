from com.ek.base.mhxy_server import MhxyServer

import pyautogui
import win32gui
import win32api
import win32con

# server1 = MhxyServer('山东1区', '南天门', '倾心醉客', '8904715')
server1 = MhxyServer('江苏3区', '花果山', '测001号', '43640727')
print(server1.to_str())

# server1.fly_jiudian()

user_name_temp = '梦幻西游 ONLINE - ({}[{}] - {}[{}])'

# user_name = '梦幻西游 ONLINE - (山东1区[南天门] - 女。子。[23236601])'
user_name = user_name_temp.format('江苏3区', '花果山', '测001号', '43640727')
# user_name = '新标签页 - Google Chrome'
mhxy_handle = win32gui.FindWindow(0, user_name)
print(mhxy_handle)
# res = win32gui.SetForegroundWindow(mhxy_handle)
# print(res)
pyautogui.FAILSAFE = False
pyautogui.PAUSE = 1

print('xxxxxxxxxxxxxxxx')
# pyautogui.click(button='right')

pyautogui.hotkey('alt', 'W')
# pyautogui.press(['x', 'y'])
