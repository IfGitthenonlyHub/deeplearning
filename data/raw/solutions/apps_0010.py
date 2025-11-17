import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Zm9yIF8gaW4gcmFuZ2UoaW50KGlucHV0KCkpKToKICAgIG4gPSBpbnQoaW5wdXQoKSkKICAgIHAgPSB0dXBsZShtYXAoaW50LCBpbnB1dCgpLnNwbGl0KCkpKQogICAgYW5zID0gW3BbaV0gZm9yIGkgaW4gcmFuZ2UobikgaWYgaSBpbiAoMCwgbiAtIDEpIG9yIHBbaV0gIT0gc29ydGVkKHBbaSAtIDE6aSArIDJdKVsxXV0KICAgIHByaW50KGxlbihhbnMpKQogICAgcHJpbnQoKmFucyk=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
