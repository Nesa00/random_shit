import win32api
import win32gui
import win32con

# Define a function to create a notification
def show_notification(title, message):
    # Create a class for the notification window
    class_name = "NotificationWindow"
    message_map = {win32con.WM_DESTROY: win32gui.PostQuitMessage}
    wc = win32gui.WNDCLASS()
    wc.lpfnWndProc = message_map
    wc.lpszClassName = class_name
    hinst = wc.hInstance = win32api.GetModuleHandle(None)
    class_atom = win32gui.RegisterClass(wc)

    # Create the notification window
    hwnd = win32gui.CreateWindow(class_atom, class_name, 0, 0, 0, 0, 0, 0, 0, hinst, None)
    hicon = win32gui.LoadIcon(0, win32con.IDI_APPLICATION)
    nid = (hwnd, 0, win32gui.NIF_ICON, win32con.WM_USER + 20, hicon, title)
    win32gui.Shell_NotifyIcon(win32gui.NIM_ADD, nid)
    win32gui.Shell_NotifyIcon(win32gui.NIM_MODIFY, (hwnd, 0, win32gui.NIF_INFO, win32con.WM_USER + 20, hicon, title, message, 200, title))

    # Destroy the notification after a delay
    win32gui.PumpMessages()
    win32gui.Shell_NotifyIcon(win32gui.NIM_DELETE, nid)
    win32gui.DestroyWindow(hwnd)
    win32gui.UnregisterClass(class_atom, hinst)

# Show a notification with a title and message
show_notification("FPGA Unlocking", "E-mail with key received")
