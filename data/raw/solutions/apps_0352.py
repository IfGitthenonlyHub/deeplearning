import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbG9uZ2VzdFN0ckNoYWluKHNlbGYsIHdvcmRzOiBMaXN0W3N0cl0pIC0+IGludDoKICAgICAgICBkcCA9IHt9CiAgICAgICAgZm9yIHcgaW4gc29ydGVkKHdvcmRzLCBrZXk9bGVuKToKICAgICAgICAgICAgZHBbd10gPSBtYXgoZHAuZ2V0KHdbOmldICsgd1tpICsgMTpdLCAwKSArIDEgZm9yIGkgaW4gcmFuZ2UobGVuKHcpKSkKICAgICAgICByZXR1cm4gbWF4KGRwLnZhbHVlcygpKQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
