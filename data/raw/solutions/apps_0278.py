import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbGFyZ2VzdE11bHRpcGxlT2ZUaHJlZShzZWxmLCBkaWdpdHM6IExpc3RbaW50XSkgLT4gc3RyOgogICAgICAgIGRwID0gWy0xLCAtMSwgLTFdCiAgICAgICAgZm9yIHggaW4gc29ydGVkKGRpZ2l0cylbOjotMV06CiAgICAgICAgICAgIGZvciBhIGluIGRwWzpdICsgWzBdOgogICAgICAgICAgICAgICAgeSA9IGEgKiAxMCArIHgKICAgICAgICAgICAgICAgIGRwW3kgJSAzXSA9IG1heChkcFt5ICUgM10sIHkpCiAgICAgICAgcmV0dXJuIHN0cihkcFswXSkgaWYgZHBbMF0gPj0gMCBlbHNlICcn").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
