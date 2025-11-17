import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbWF4U2l6ZVNsaWNlcyhzZWxmLCBzbGljZXM6IExpc3RbaW50XSkgLT4gaW50OgogICAgICAgIG49bGVuKHNsaWNlcykKICAgICAgICBpZHggPSBtaW4ocmFuZ2UobiksIGtleT1sYW1iZGEgeDogc2xpY2VzW3hdKQogICAgICAgIHNsaWNlcyA9IHNsaWNlc1tpZHgrMTpdICsgc2xpY2VzWzppZHhdCiAgICAgICAgQGxydV9jYWNoZShOb25lKQogICAgICAgIGRlZiBkcChpLGspOgogICAgICAgICAgICBpZiBpPj1uLTEgb3Igaz09MDoKICAgICAgICAgICAgICAgIHJldHVybiAwCiAgICAgICAgICAgIHJldHVybiBtYXgoc2xpY2VzW2ldK2RwKGkrMixrLTEpLGRwKGkrMSxrKSkKICAgICAgICByZXR1cm4gZHAoMCxuLy8zKQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
