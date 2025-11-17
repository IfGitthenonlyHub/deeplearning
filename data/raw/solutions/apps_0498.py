import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgZGVmIHJvYihzZWxmLCBudW1zKToKICAgICAgICAgIiIiCiAgICAgICAgIDp0eXBlIG51bXM6IExpc3RbaW50XQogICAgICAgICA6cnR5cGU6IGludAogICAgICAgICAiIiIKICAgICAgICAgaWYgbGVuKG51bXMpPT0xOiByZXR1cm4gbnVtc1swXQogICAgICAgICBsYXN0LCBub3c9IDAsIDAKICAgICAgICAgZm9yIGkgaW4gbnVtc1s6LTFdOiBsYXN0LCBub3cgPSBub3csIG1heChsYXN0K2ksIG5vdykKICAgICAgICAgcmV0PW5vdwogICAgICAgICBsYXN0LCBub3c9IDAsIDAKICAgICAgICAgZm9yIGkgaW4gbnVtc1sxOl06IGxhc3QsIG5vdyA9IG5vdywgbWF4KGxhc3QraSwgbm93KQogICAgICAgICByZXR1cm4gbWF4KHJldCwgbm93KQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
