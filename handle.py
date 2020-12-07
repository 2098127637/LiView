import sys
import win32com.client

shell = win32com.client.Dispatch("WScript.Shell")
shortcut = shell.CreateShortCut("C:\Users\Public\Desktop\人工桌面")
print(shortcut.Targetpath)