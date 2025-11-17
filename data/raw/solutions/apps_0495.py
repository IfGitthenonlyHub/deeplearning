import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbGFzdFN0b25lV2VpZ2h0SUkoc2VsZiwgc3RvbmVzOiBMaXN0W2ludF0pIC0+IGludDoKICAgICAgICBkcCA9IHswfQogICAgICAgIHRvdGFsID0gc3VtKHN0b25lcykKICAgICAgICBmb3Igc3RvbmUgaW4gc3RvbmVzOgogICAgICAgICAgICBkcCB8PSB7X3N1bSArIHN0b25lIGZvciBfc3VtIGluIGRwfQogICAgICAgIHJldHVybiBtaW4oYWJzKHRvdGFsIC0gX3N1bSAtIF9zdW0pIGZvciBfc3VtIGluIGRwKQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
