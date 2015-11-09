from win32api import GetCursorPos
from win32api import GetSystemMetrics
import string , sys , vim , win32gui

resolution_w = GetSystemMetrics(0)
if string.atoi(vim.eval("g:enable_vim_wm_taskbar")) == 1:
    resolution_h = GetSystemMetrics(1) - 30
else:
    resolution_h = GetSystemMetrics(1)
hwnd = win32gui.GetActiveWindow()
win_rect = win32gui.GetWindowRect(hwnd)
win_rect_x = win_rect[0]
win_rect_y = win_rect[1]
win_rect_w = win_rect[2] - win_rect_x
win_rect_h = win_rect[3] - win_rect_y
center_x = (resolution_w - win_rect_w) / 2
center_y = (resolution_h - win_rect_h) / 2
smart_x = [resolution_w / 3 , resolution_w / 3 * 2 , resolution_w , resolution_w - win_rect_w]
smart_y = [resolution_h / 3 , resolution_h / 3 * 2 , resolution_h , resolution_h - win_rect_h]
wincenter = GetCursorPos()
if string.atoi(vim.eval("g:enable_vim_wm_smartsize")) == 1:
    big = [resolution_w / 3 * 2 , resolution_h / 3 * 2]
    large = [resolution_w / 5 * 4 , resolution_h / 5 * 4]
else:
    big = [string.atoi(vim.eval("g:vim_wm_big[0]")) , string.atoi(vim.eval("g:vim_wm_big[1]"))]
    large = [string.atoi(vim.eval("g:vim_wm_large[0]")) , string.atoi(vim.eval("g:vim_wm_large[1]"))]

def win_pos(x,y,z):
    win32gui.SetWindowPos(hwnd, 0, x, y, 0, 0, 0x0001 + 0x0004)
    vim.command("echo 'Position ='"+str(z))

def win_size(x,y):
    a = (resolution_w - x) / 2
    b = (resolution_h - y) / 2
    win32gui.SetWindowPos(hwnd, 0, a, b, x, y, 0x0004)
    vim.command("echo 'Position = 5 ; Size ='"+str(x)+" "+str(y))

class win_move:
    def position1(self):
        win_pos(0,smart_y[3],1)
    def position4(self):
        win_pos(0,center_y,4)
    def position7(self):
        win_pos(0,0,7)
    def position2(self):
        win_pos(center_x,smart_y[3],2)
    def position5(self):
        win_pos(center_x,center_y,5)
    def position8(self):
        win_pos(center_x,0,8)
    def position3(self):
        win_pos(smart_x[3],smart_y[3],3)
    def position6(self):
        win_pos(smart_x[3],center_y,6)
    def position9(self):
        win_pos(smart_x[3],0,9)

def smartposition():
    if wincenter[0] >= 0 and wincenter[0] <= smart_x[0]:
        if wincenter[1] <= smart_y[0]:
            wm.position7()
        elif wincenter[1] >= smart_y[0] and wincenter[1] <= smart_y[1]:
            wm.position4()
        elif wincenter[1] >= smart_y[1] and wincenter[1] <= smart_y[2]:
            wm.position1()
    elif wincenter[0] >= smart_x[0] and wincenter[0] <= smart_x[1]:
        if wincenter[1] <= smart_y[0]:
            wm.position8()
        elif wincenter[1] >= smart_y[0] and wincenter[1] <= smart_y[1]:
            wm.position5()
        elif wincenter[1] >= smart_y[1] and wincenter[1] <= smart_y[2]:
            wm.position2()
    elif wincenter[0] >= smart_x[1] and wincenter[0] <= smart_x[2]:
        if wincenter[1] <= smart_y[0]:
            wm.position9()
        elif wincenter[1] >= smart_y[0] and wincenter[1] <= smart_y[1]:
            wm.position6()
        elif wincenter[1] >= smart_y[1] and wincenter[1] <= smart_y[2]:
            wm.position3()

def size_default():
    vim.command("set columns=80")
    vim.command("set lines=25")
    vim.command("winpos 0 0")
    vim.command("echo 'Position+Size = Default'")

def size_big():
    win_size(big[0] , big[1])

def size_large():
    win_size(large[0] , large[1])

wm = win_move()
selectmode = {'smart': smartposition,
              'default': size_default,
              'big': size_big,
              'large': size_large,
}
selectmode[sys.argv[0]]()
