import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbWluSW5jcmVtZW50Rm9yVW5pcXVlKHNlbGYsIEEpOgogICAgICAgIHJlcyA9IG5lZWQgPSAwCiAgICAgICAgZm9yIGkgaW4gc29ydGVkKEEpOgogICAgICAgICAgICByZXMgKz0gbWF4KG5lZWQgLSBpLCAwKQogICAgICAgICAgICBuZWVkID0gbWF4KG5lZWQgKyAxLCBpICsgMSkKCiAgICAgICAgcmV0dXJuIHJlcw==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
