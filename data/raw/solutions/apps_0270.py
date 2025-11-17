import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgZ2V0SGFwcHlTdHJpbmcoc2VsZiwgbjogaW50LCBrOiBpbnQpIC0+IHN0cjoKICAgICAgICBuZXh0TGV0dGVyID0geydhJzonYmMnLCdiJzonYWMnLCdjJzonYWInfQogICAgICAgIHEgPSBkZXF1ZShbJ2EnLCdiJywnYyddKQogICAgICAgIHdoaWxlIGxlbihxWzBdKSAhPSBuOgogICAgICAgICAgICB1ID0gcS5wb3BsZWZ0KCkKICAgICAgICAgICAgZm9yIHYgaW4gbmV4dExldHRlclt1Wy0xXV06CiAgICAgICAgICAgICAgICBxLmFwcGVuZCh1ICsgdikKICAgICAgICByZXR1cm4gcVtrIC0gMV0gaWYgbGVuKHEpID49IGsgZWxzZSAnJw==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
