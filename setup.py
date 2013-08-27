import sys
from cx_Freeze import setup, Executable

buildOptions = dict(
        compressed = True,
        includes = ["atexit"],
#         excludes = ['tk', '_tkagg', '_gtkagg', '_gtk', 'tcl'],
        # include_files = [(matplotlib.get_data_path(), "mpl-data")],
        path = sys.path)

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
        name="LEDMatrixCodeGenerate",
        version="0.1",
        description="Image Mass Spectrum",
        options=dict(build_exe=buildOptions),
        executables=[Executable("Main.py", base=base)])
