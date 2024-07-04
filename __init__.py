from __future__ import annotations

try:
    from .cyfragmentparser import *

except Exception as e:
    import Cython, setuptools, flatten_any_dict_iterable_or_whatsoever, pandas, numpy, parifinder, nested2nested, platform, subprocess, os, sys, time

    iswindows = "win" in platform.platform().lower()
    if iswindows:
        addtolist = []
    else:
        addtolist = ["&"]

    olddict = os.getcwd()
    dirname = os.path.dirname(__file__)
    os.chdir(dirname)
    compile_file = os.path.join(dirname, "cyfragmentparser_compile.py")
    subprocess.run(
        " ".join([sys.executable, compile_file, "build_ext", "--inplace"] + addtolist),
        shell=True,
        env=os.environ,
        preexec_fn=None if iswindows else os.setpgrp,
    )
    if not iswindows:
        time.sleep(30)
    from .cyfragmentparser import *

    os.chdir(olddict)
