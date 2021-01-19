import win32gui
import pyautogui

# user_name = '梦幻西游 ONLINE - (江苏3区[花果山] - 小凌波°[42645587])'

user_name_temp = '梦幻西游 ONLINE - ({}[{}] - {}[{}])'

# user_name = '梦幻西游 ONLINE - (山东1区[南天门] - 女。子。[23236601])'
user_name = user_name_temp.format('江苏3区', '花果山', '测001号', '43640727')

print(user_name)
mhxy_handle = win32gui.FindWindow(0, user_name)
print(mhxy_handle)

if mhxy_handle > 0:
    class_name = win32gui.GetClassName(mhxy_handle)
    print(class_name)
    title = win32gui.GetWindowText(mhxy_handle)
    print(title)
    win32gui.SetForegroundWindow(mhxy_handle)

    pyautogui.PAUSE = 1
    pyautogui.hotkey('alt', 'e')

    left, top, right, bottom = win32gui.GetWindowRect(mhxy_handle)
    print(left)
    print(top)
    # 260 330
    flying_flay_changan_x, flying_flay_changan_y = left + 260, top + 330
    print(flying_flay_changan_x)
    print(flying_flay_changan_y)
    pyautogui.moveTo(flying_flay_changan_x, flying_flay_changan_y, 0.5)
    pyautogui.click(button='right')

    # 310 25
    jiudian_x, jiudian_y = flying_flay_changan_x + 313, flying_flay_changan_y - 34
    pyautogui.moveTo(jiudian_x, jiudian_y, 0.5)
    pyautogui.click(button='left')


else:
    print('获取句柄失败')
