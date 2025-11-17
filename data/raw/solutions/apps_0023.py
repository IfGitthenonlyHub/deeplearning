import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("aW1wb3J0IHN5cwppbnB1dCA9IHN5cy5zdGRpbi5yZWFkbGluZQppbXBvcnQgaGVhcHEgYXMgaHEKdCA9IGludChpbnB1dCgpKQpmb3IgXyBpbiByYW5nZSh0KToKICBuID0gaW50KGlucHV0KCkpCiAgdnQgPSBbbGlzdChtYXAoaW50LGlucHV0KCkuc3BsaXQoKSkpIGZvciBpIGluIHJhbmdlKG4pXQogIHZ0LnNvcnQocmV2ZXJzZT1UcnVlKQogIHEgPSBbXQogIGhxLmhlYXBpZnkocSkKICBhbnMgPSAwCiAgY250ID0gMAogIGZvciBpIGluIHJhbmdlKG4pOgogICAgaHEuaGVhcHB1c2gocSx2dFtpXVsxXSkKICAgIGlmIHZ0W2ldWzBdID49IG4taStjbnQ6CiAgICAgIGFucyArPSBocS5oZWFwcG9wKHEpCiAgICAgIGNudCArPSAxCiAgcHJpbnQoYW5zKQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
