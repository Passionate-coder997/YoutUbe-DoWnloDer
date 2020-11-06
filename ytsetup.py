import sys
from cx_Freeze import setup,Executable

base=None

if sys.platform=='win32':
	base="Win32GUI"

executables = [Executable("ytdownloader.py", base=base, targetName="Download Anything from Youtube")]

setup(options = {"build.exe": {"packages" : ["tkinter"]}},
	version = "1.0",
	discription = "Youtube Downloader",
	executables = executables
	)