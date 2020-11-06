import sys
from cx_Freeze import setup,Executable

base=None

if sys.platform=='win32':
	base="Win32GUI"

executables = [Executable("Youtube download(GUI).py", icon='yticon.ico', base=base, targetName="Youtube Downloader")]

setup(options = {"build.exe": {"packages" : ["tkinter"], "include files": ["yticon.ico"]}},
	version = "1.0",
	discription = "Youtube downloader",
	executables = executables
	)