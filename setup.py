import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name = "Turtle Adventures",
    version = "0.1",
    description = "Turtle Adventures Dev Version",
    options = {"build_exe": build_exe_options},
    executables = [Executable("main.py", base=base)]
)