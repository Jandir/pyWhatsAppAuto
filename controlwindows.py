import win32gui
import re
import pyautogui

class WindowMgr:
    """Encapsulates some calls to the winapi for window management"""

    def __init__ (self):
        """Constructor"""
        self._handle = None

    def find_window(self, class_name, window_name=None):
        """find a window by its class_name"""
        self._handle = win32gui.FindWindow(class_name, window_name)

    def _window_enum_callback(self, hwnd, wildcard):
        """Pass to win32gui.EnumWindows() to check all the opened windows"""
        if re.match(wildcard, str(win32gui.GetWindowText(hwnd))) is not None:
            self._handle = hwnd

    def find_window_wildcard(self, wildcard):
        """find a window whose title matches the wildcard regex"""
        self._handle = None
        win32gui.EnumWindows(self._window_enum_callback, wildcard)

    def set_foreground(self):
        """put the window in the foreground"""
        win32gui.SetForegroundWindow(self._handle)


w = WindowMgr()
w.find_window_wildcard(".*WhatsApp.*")
w.set_foreground()

texto = 'O grupo VIP *Vencendo as Batalhas Espirituais* 🥇🏆 tem o propósito de disponibilizar a condição ÚNICA e EXCLUSIVA para você se inscrever na condição especial da imersão presencial. \
Atenção para o cronograma ✨ \
\
▶ 10/02 às 9h: A equipe do AP. Fernando Guillen informará qual é a condição especial. \
▶ 11/02 às 9h: Abriremos as inscrições, informando o link de compra, que ficará disponível até as 21h ou até que as vagas disponíveis se esgotem. \
\
Fique atento as notificações do grupo 🙂 \
\
Equipe Equipe AP. Fernando Guillen'

import emoji

