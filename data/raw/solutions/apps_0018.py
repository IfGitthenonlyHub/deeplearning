import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("dD1pbnQoaW5wdXQoKSkKaW1wb3J0IG1hdGggYXMgbQp3aGlsZSB0OgogICAgdC09MQogICAgYT1pbnQoaW5wdXQoKSkKICAgIHByaW50KDEvKG0udGFuKG0ucGkvKDIqYSkpKSk=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
