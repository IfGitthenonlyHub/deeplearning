import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("aW1wb3J0IG1hdGgKZm9yIF8gaW4gcmFuZ2UoaW50KGlucHV0KCkpKToKIG49aW50KGlucHV0KCkpCiBzPWludChtYXRoLnNxcnQobikpCiBhbnM9MAogZm9yIGkgaW4gcmFuZ2UoMSxzKzEpOgogIGFucys9KG4vL2kpCiBhbnM9YW5zKjItKHMqcykKIGc9bWF0aC5nY2QobipuLGFucykKIHByaW50KHN0cihhbnMvL2cpKyIvIitzdHIobipuLy9nKSk=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
