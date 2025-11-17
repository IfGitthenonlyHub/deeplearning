import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("dCA9IGludChpbnB1dCgpKQoKZm9yIF8gaW4gcmFuZ2UodCk6CiAgICBuLCBxID0gbGlzdChtYXAoaW50LCBpbnB1dCgpLnNwbGl0KCkpKQogICAgCiAgICBhID0gbGlzdChtYXAoaW50LCBpbnB1dCgpLnNwbGl0KCkpKQogICAgCiAgICBiZXN0X3AgPSBiZXN0X20gPSAwCiAgICAKICAgIGZvciB4IGluIGE6CiAgICAgICAgYmVzdF9wID0gbWF4KGJlc3RfcCwgYmVzdF9tIC0geCkKICAgICAgICBiZXN0X20gPSBtYXgoYmVzdF9tLCBiZXN0X3AgKyB4KQogICAgICAgIAogICAgcHJpbnQobWF4KGJlc3RfcCwgYmVzdF9tKSk=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
