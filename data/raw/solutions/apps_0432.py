import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgaXNQb3NzaWJsZURpdmlkZShzZWxmLCBudW1zOiBMaXN0W2ludF0sIGs6IGludCkgLT4gYm9vbDoKICAgICAgICBjID0gQ291bnRlcihudW1zKQogICAgICAgIHdoaWxlIGM6CiAgICAgICAgICAgIHggPSBtaW4oYy5rZXlzKCkpCiAgICAgICAgICAgIGZvciBpIGluIHJhbmdlKHgseCtrKToKICAgICAgICAgICAgICAgIGlmIGkgbm90IGluIGM6IHJldHVybiBGYWxzZQogICAgICAgICAgICAgICAgY1tpXSAtPSAxCiAgICAgICAgICAgICAgICBpZiBjW2ldID09IDA6IGRlbCBjW2ldCiAgICAgICAgcmV0dXJuIFRydWU=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
