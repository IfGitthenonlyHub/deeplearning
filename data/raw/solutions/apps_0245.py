import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgZGVmIG9wdGltYWxEaXZpc2lvbihzZWxmLCBudW1zKToKICAgICAgICAgIiIiCiAgICAgICAgIDp0eXBlIG51bXM6IExpc3RbaW50XQogICAgICAgICA6cnR5cGU6IHN0cgogICAgICAgICAiIiIKICAgICAgICAgQSA9IGxpc3QobWFwKHN0ciwgbnVtcykpCiAgICAgICAgIGlmIGxlbihBKSA8PSAyOgogICAgICAgICAgICAgcmV0dXJuICcvJy5qb2luKEEpCiAgICAgICAgIHJldHVybiBBWzBdICsgJy8oJyArICcvJy5qb2luKEFbMTpdKSArICcpJw==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
