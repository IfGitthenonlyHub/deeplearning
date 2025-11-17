import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgZGVmIGlzU2VsZkNyb3NzaW5nKHNlbGYsIHgpOgogICAgICAgICAiIiIKICAgICAgICAgOnR5cGUgeDogTGlzdFtpbnRdCiAgICAgICAgIDpydHlwZTogYm9vbAogICAgICAgICAiIiIKICAgICAgICAgYiA9IGMgPSBkID0gZSA9IDAKICAgICAgICAgZm9yIGEgaW4geDoKICAgICAgICAgICAgIGlmIGQgPj0gYiA+IDAgYW5kIChhID49IGMgb3IgYSA+PSBjLWUgPj0gMCBhbmQgZiA+PSBkLWIpOgogICAgICAgICAgICAgICAgIHJldHVybiBUcnVlCiAgICAgICAgICAgICBiLCBjLCBkLCBlLCBmID0gYSwgYiwgYywgZCwgZQogICAgICAgICByZXR1cm4gRmFsc2U=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
