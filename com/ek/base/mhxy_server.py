import win32gui
import pyautogui
from com.ek.error.param_error import ParamError

user_name_temp = '梦幻西游 ONLINE - ({}[{}] - {}[{}])'


class MhxyServer:
    """
    梦幻西游服务器及角色信息
    """
    regional = None
    server = None
    user_name = None
    user_id = None
    mh_handle = None

    def __init__(self, regional, server, user_name, user_id):
        """
        :param regional:    大区名字，如：山东4区
        :param server:      服务器名字，沂水雪山
        :param user_name:   角色名，张三
        :param user_id:     角色ID，23236601
        """
        print('init')
        if regional is None:
            raise ParamError('Param [regional] is None')
        if server is None:
            raise ParamError('Param [server] is None')
        if user_name is None:
            raise ParamError('Param [user_name] is None')
        if user_id is None:
            raise ParamError('Param [user_id] is None')
        self.regional = regional
        self.server = server
        self.user_name = user_name
        self.user_id = user_id

    def to_str(self):
        return self.__dict__

    def _active_window(self):
        user_name = user_name_temp.format(self.regional, self.server, self.user_name, self.user_id)
        self.mh_handle = win32gui.FindWindow(0, user_name)
        if self.mh_handle <= 0:
            print('未获取到句柄窗口')
            return False
        win32gui.SetForegroundWindow(self.mh_handle)
        return True

    def fly_jiudian(self):
        if not self._active_window():
            return False
        pyautogui.PAUSE = 1
        pyautogui.hotkey('alt', 'e')

        left, top, right, bottom = win32gui.GetWindowRect(self.mh_handle)
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

        return True
