import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbWN0RnJvbUxlYWZWYWx1ZXMoc2VsZiwgYXJyOiBMaXN0W2ludF0pIC0+IGludDoKICAgICAgICByZXMgPSAwCiAgICAgICAgCiAgICAgICAgd2hpbGUgKGxlbihhcnIpID4gMSk6CiAgICAgICAgCiAgICAgICAgICAgIG1pZCA9IGFyci5pbmRleChtaW4oYXJyKSkKICAgICAgICAgICAgCiAgICAgICAgICAgIHJlcyArPSBtaW4oYXJyW21pZCAtIDE6bWlkXSArIGFyclttaWQrMTptaWQgKyAyXSkgKiBhcnIucG9wKG1pZCkKICAgICAgICAKICAgCiAgICAgICAgcmV0dXJuIHJlcw==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
