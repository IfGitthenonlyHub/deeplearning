import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgZXF1YWxTdWJzdHJpbmcoc2VsZiwgczogc3RyLCB0OiBzdHIsIG1heENvc3Q6IGludCkgLT4gaW50OgogICAgICAgIGkgPSAwCiAgICAgICAgZm9yIGogaW4gcmFuZ2UobGVuKHMpKToKICAgICAgICAgICAgbWF4Q29zdCAtPSBhYnMob3JkKHNbal0pIC0gb3JkKHRbal0pKQogICAgICAgICAgICBpZiBtYXhDb3N0IDwgMDoKICAgICAgICAgICAgICAgIG1heENvc3QgKz0gYWJzKG9yZChzW2ldKSAtIG9yZCh0W2ldKSkKICAgICAgICAgICAgICAgIGkgKz0gMQogICAgICAgIHJldHVybiBqIC0gaSArIDE=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
