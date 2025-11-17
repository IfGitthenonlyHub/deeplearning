import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbWF4U2NvcmUoc2VsZiwgcDogTGlzdFtpbnRdLCBrOiBpbnQpIC0+IGludDoKICAgICAgICByZXMgPSBzdW0ocFs6a10pCiAgICAgICAgY3VyID0gcmVzCiAgICAgICAgCiAgICAgICAgZm9yIGkgaW4gcmFuZ2UoMSwgaysxKToKICAgICAgICAgICAgY3VyICs9IHBbLWldIC0gcFtrLWldCiAgICAgICAgICAgIHJlcyA9IG1heChjdXIsIHJlcykKICAgICAgICAKICAgICAgICByZXR1cm4gcmVz").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
