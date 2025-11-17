import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("YSA9IGludChpbnB1dCgpKQpmb3IgaSBpbiByYW5nZShhKToKICAgIHMxID0gc2V0KCkKICAgIGFucyA9IDAKICAgIGwgPSBpbnB1dCgpCiAgICBub3cgPSBpbnB1dCgpLnNwbGl0KCkKICAgIGZvciBpIGluIG5vdzoKICAgICAgICBrID1pbnQoaSkgCiAgICAgICAgd2hpbGUgayUyPT0wIGFuZCBrIG5vdCBpbiBzMToKICAgICAgICAgICAgczEuYWRkKGspCiAgICAgICAgICAgIGs9ay8vMgogICAgcHJpbnQobGVuKHMxKSk=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
