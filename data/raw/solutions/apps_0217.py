import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgc3ViYXJyYXlCaXR3aXNlT1JzKHNlbGYsIEE6IExpc3RbaW50XSkgLT4gaW50OgogICAgICAgIHMsIGFucyA9IHNldCgpLCBzZXQoKQogICAgICAgIGZvciBhIGluIEE6CiAgICAgICAgICAgIHMgPSB7YX0gfCB7YSB8IGIgZm9yIGIgaW4gc30KICAgICAgICAgICAgYW5zIHw9IHMKICAgICAgICByZXR1cm4gbGVuKGFucyk=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
