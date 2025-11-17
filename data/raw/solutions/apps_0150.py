import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgcGFydGl0aW9uRGlzam9pbnQoc2VsZiwgQTogTGlzdFtpbnRdKSAtPiBpbnQ6CiAgICAgICAgYW5zID0gMQogICAgICAgIGFsbF9tYXggPSBBWzBdCiAgICAgICAgY3Vycl9tYXggPSAwCiAgICAgICAgZm9yIGkgaW4gcmFuZ2UobGVuKEEpKToKICAgICAgICAgICAgY3Vycl9tYXggPSBtYXgoY3Vycl9tYXgsIEFbaV0pCiAgICAgICAgICAgIGlmIGFsbF9tYXggPiBBW2ldOgogICAgICAgICAgICAgICAgYWxsX21heCA9IGN1cnJfbWF4CiAgICAgICAgICAgICAgICBhbnMgPSBpICsgMQogICAgICAgIHJldHVybiBhbnM=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
