import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbWF4Vm93ZWxzKHNlbGYsIHM6IHN0ciwgazogaW50KSAtPiBpbnQ6CiAgICAgICAgbWF4Vm93LCBjb3VudCA9IDAsIDAKICAgICAgICBmb3IgaSwgaiBpbiBlbnVtZXJhdGUocyk6CiAgICAgICAgICAgIGlmIGogaW4gJ2FlaW91JzoKICAgICAgICAgICAgICAgIGNvdW50ICs9IDEKICAgICAgICAgICAgaWYgaSA+PSBrIGFuZCBzW2kta10gaW4gJ2FlaW91JzoKICAgICAgICAgICAgICAgIGNvdW50IC09IDEKICAgICAgICAgICAgbWF4Vm93ID0gbWF4KG1heFZvdywgY291bnQpCiAgICAgICAgcmV0dXJuIG1heFZvdw==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
