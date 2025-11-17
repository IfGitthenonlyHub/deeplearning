import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgZGllU2ltdWxhdG9yKHNlbGYsIG46IGludCwgcm9sbE1heDogTGlzdFtpbnRdKSAtPiBpbnQ6CiAgICAgICAgYSxiLG09W2RlcXVlKFswXSp4KSBmb3IgeCBpbiByb2xsTWF4XSxbMV0qNiwxMDAwMDAwMDA3CiAgICAgICAgZm9yIHggaW4gYTogeFstMV09MQogICAgICAgIGZvciBfIGluIHJhbmdlKG4tMSk6CiAgICAgICAgICAgIHM9c3VtKGIpJW0KICAgICAgICAgICAgZm9yIGkseCBpbiBlbnVtZXJhdGUoYSk6CiAgICAgICAgICAgICAgICB4LmFwcGVuZCgocy1iW2ldKSVtKQogICAgICAgICAgICAgICAgYltpXT0oYltpXSt4Wy0xXS14LnBvcGxlZnQoKSklbQogICAgICAgIHJldHVybiBzdW0oYiklbQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
