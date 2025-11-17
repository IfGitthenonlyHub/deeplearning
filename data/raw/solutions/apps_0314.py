import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbnVtU3ViKHNlbGYsIHM6IHN0cikgLT4gaW50OgogICAgICAgIHN1bSA9IGNudCA9IDAKICAgICAgICBmb3IgYyBpbiBzOgogICAgICAgICAgICBpZiBjID09ICcxJzoKICAgICAgICAgICAgICAgIGNudCArPSAxCiAgICAgICAgICAgICAgICBzdW0gPSAoc3VtICsgY250KSAlICgxMCAqKiA5ICsgNykKICAgICAgICAgICAgZWxzZToKICAgICAgICAgICAgICAgIGNudCA9IDAKICAgICAgICByZXR1cm4gc3Vt").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
