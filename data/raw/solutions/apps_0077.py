import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("ZnJvbSBtYXRoIGltcG9ydCBpbmYgYXMgaW5mCmltcG9ydCBzeXMKZm9yIF8gaW4gcmFuZ2UoaW50KGlucHV0KCkpKToKICAgIG49aW50KHN5cy5zdGRpbi5yZWFkbGluZSgpKQogICAgZHAgPSBbW2luZixpbmYsaW5mXSBmb3IgXyBpbiByYW5nZShuKzEpXQogICAgYXJyID0gW10KICAgIGZvciBpIGluIHJhbmdlKG4pOgogICAgICAgIGFyci5hcHBlbmQobGlzdChtYXAoaW50LHN5cy5zdGRpbi5yZWFkbGluZSgpLnNwbGl0KCkpKSkKICAgIGRwWzBdID0gWzAsYXJyWzBdWzFdLGFyclswXVsxXSoyXQogICAgCiAgICBmb3IgaSBpbiByYW5nZSgxLG4pOgogICAgICAgIGZvciBqIGluIHJhbmdlKDMpOgogICAgICAgICAgICBmb3IgayBpbiByYW5nZSgzKToKICAgICAgICAgICAgICAgIGlmIGFycltpXVswXStqIT1hcnJbaS0xXVswXStrOgogICAgICAgICAgICAgICAgICAgIGRwW2ldW2pdID0gbWluKGRwW2ldW2pdLGRwW2ktMV1ba10raiphcnJbaV1bMV0pCiAgICBwcmludChtaW4oZHBbbi0xXSkp").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
