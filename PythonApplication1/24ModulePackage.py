#There are 3 different ways to import document:
#1) the classic one, using standard directory in the sys.path list
import sys
#2) Packages import where the used directory is relative located to the sys.path list
import importing.FuncTest as ooo
#3) Relative only. Are path relative onlyto the package directory [sys.path is not used]
#modules intended for use as the main module of a Python application must always use absolute imports.
#Look in importing.FuncTest code.
#-->    from .importing.PrintOnImport import Pippo as pip
#-->    from .importing import Changer
