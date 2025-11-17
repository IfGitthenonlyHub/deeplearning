import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgY2hlY2tJZkNhbkJyZWFrKHNlbGYsIHMxLCBzMik6CiAgICAgICAgczEgPSBzb3J0ZWQoczEpCiAgICAgICAgczIgPSBzb3J0ZWQoczIpCiAgICAgICAgcmV0dXJuIGFsbCh4IDw9IHkgZm9yIHgsIHkgaW4gemlwKHMxLCBzMikpIG9yIGFsbCh5IDw9IHggZm9yIHgsIHkgaW4gemlwKHMxLCBzMikp").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
