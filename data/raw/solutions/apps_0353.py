import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbnVtU3Vic2VxKHNlbGYsIEEsIHRhcmdldCk6CiAgICAgICAgQS5zb3J0KCkKICAgICAgICBsLCByID0gMCwgbGVuKEEpIC0gMQogICAgICAgIHJlcyA9IDAKICAgICAgICBtb2QgPSAxMCoqOSArIDcKICAgICAgICB3aGlsZSBsIDw9IHI6CiAgICAgICAgICAgIGlmIEFbbF0gKyBBW3JdID4gdGFyZ2V0OgogICAgICAgICAgICAgICAgciAtPSAxCiAgICAgICAgICAgIGVsc2U6CiAgICAgICAgICAgICAgICByZXMgKz0gcG93KDIsIHIgLSBsLCBtb2QpCiAgICAgICAgICAgICAgICBsICs9IDEKICAgICAgICByZXR1cm4gcmVzICUgbW9k").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
