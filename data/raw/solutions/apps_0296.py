import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgZGVmIGZpbmRNaW4oc2VsZiwgbnVtcyk6CiAgICAgICAgICIiIgogICAgICAgICA6dHlwZSBudW1zOiBMaXN0W2ludF0KICAgICAgICAgOnJ0eXBlOiBpbnQKICAgICAgICAgIiIiCiAgICAgICAgIG1pbl9uID0gbnVtc1swXQogICAgICAgICBmb3IgbiBpbiBudW1zOgogICAgICAgICAgICAgaWYgbiA8IG1pbl9uOgogICAgICAgICAgICAgICAgIG1pbl9uID0gbgogICAgICAgICByZXR1cm4gbWluX24=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
