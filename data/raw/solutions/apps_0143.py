import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgdG90YWxGcnVpdChzZWxmLCB0cmVlKToKICAgICAgICByZXMgPSBjdXIgPSBjb3VudF9iID0gYSA9IGIgPSAwCiAgICAgICAgZm9yIGMgaW4gdHJlZToKICAgICAgICAgICAgY3VyID0gY3VyICsgMSBpZiBjIGluIChhLCBiKSBlbHNlIGNvdW50X2IgKyAxCiAgICAgICAgICAgIGNvdW50X2IgPSBjb3VudF9iICsgMSBpZiBjID09IGIgZWxzZSAxCiAgICAgICAgICAgIGlmIGIgIT0gYzogYSwgYiA9IGIsIGMKICAgICAgICAgICAgcmVzID0gbWF4KHJlcywgY3VyKQogICAgICAgIHJldHVybiByZXM=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
