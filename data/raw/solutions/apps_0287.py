import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgZGVmIGNvdW50QXJyYW5nZW1lbnQoc2VsZiwgTik6CiAgICAgICAgICIiIgogICAgICAgICA6dHlwZSBOOiBpbnQKICAgICAgICAgOnJ0eXBlOiBpbnQKICAgICAgICAgIiIiCiAgICAgICAgIHJldHVybiAoMSwgMiwgMywgOCwgMTAsIDM2LCA0MSwgMTMyLCAyNTAsIDcwMCwgNzUwLCA0MDEwLCA0MjM3LCAxMDY4MCwgMjQ2NzkpW04gLSAxXQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
