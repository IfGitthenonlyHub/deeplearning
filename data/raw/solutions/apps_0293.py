import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgZGVmIGxlYXN0SW50ZXJ2YWwoc2VsZiwgdGFza3MsIG4pOgogICAgICAgICAiIiIKICAgICAgICAgOnR5cGUgdGFza3M6IExpc3Rbc3RyXQogICAgICAgICA6dHlwZSBuOiBpbnQKICAgICAgICAgOnJ0eXBlOiBpbnQKICAgICAgICAgIiIiCiAgICAgICAgIGwsZGljPWxlbih0YXNrcykse30KICAgICAgICAgZm9yIGMgaW4gdGFza3M6CiAgICAgICAgICAgICBpZiBjIGluIGRpYzoKICAgICAgICAgICAgICAgICBkaWNbY10rPTEKICAgICAgICAgICAgIGVsc2U6CiAgICAgICAgICAgICAgICAgZGljW2NdPTEKICAgICAgICAgbSxhPW1heChkaWMudmFsdWVzKCkpLDAKICAgICAgICAgZm9yIGMgaW4gZGljOgogICAgICAgICAgICAgaWYgZGljW2NdPT1tOgogICAgICAgICAgICAgICAgIGErPTEKICAgICAgICAgcmV0dXJuIG1heChsLChtLTEpKihuKzEpK2Ep").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
