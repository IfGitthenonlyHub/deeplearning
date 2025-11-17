import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgZmxpcGdhbWUoc2VsZiwgZnJvbnRzOiBMaXN0W2ludF0sIGJhY2tzOiBMaXN0W2ludF0pIC0+IGludDoKICAgICAgICBzYW1lID0ge3ggZm9yIHgsIHkgaW4gemlwKGZyb250cywgYmFja3MpIGlmIHggPT0geX0KICAgICAgICByZXR1cm4gbWluKFtpIGZvciBpIGluIGZyb250cyArIGJhY2tzIGlmIGkgbm90IGluIHNhbWVdIG9yIFswXSk=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
