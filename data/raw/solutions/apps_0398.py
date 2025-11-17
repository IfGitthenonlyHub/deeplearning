import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgZGVmIHN1YmFycmF5U3VtKHNlbGYsIG51bXMsIGspOgogICAgICAgICAiIiIKICAgICAgICAgOnR5cGUgbnVtczogTGlzdFtpbnRdCiAgICAgICAgIDp0eXBlIGs6IGludAogICAgICAgICA6cnR5cGU6IGludAogICAgICAgICAiIiIKICAgICAgICAgY291bnQsIGN1ciwgcmVzID0gezA6IDF9LCAwLCAwCiAgICAgICAgIGZvciB2IGluIG51bXM6CiAgICAgICAgICAgICBjdXIgKz0gdgogICAgICAgICAgICAgcmVzICs9IGNvdW50LmdldChjdXIgLSBrLCAwKQogICAgICAgICAgICAgY291bnRbY3VyXSA9IGNvdW50LmdldChjdXIsIDApICsgMQogICAgICAgICByZXR1cm4gcmVz").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
