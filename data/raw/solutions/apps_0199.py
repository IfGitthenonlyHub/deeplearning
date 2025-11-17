import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgZGVmIGxvbmdlc3RDb25zZWN1dGl2ZShzZWxmLCBudW1zKToKICAgICAgICAgIiIiCiAgICAgICAgIDp0eXBlIG51bXM6IExpc3RbaW50XQogICAgICAgICA6cnR5cGU6IGludAogICAgICAgICAiIiIKICAgICAgICAgbnVtcyA9IHNldChudW1zKQogICAgICAgICBiZXN0ID0gMAogICAgICAgICBmb3IgeCBpbiBudW1zOgogICAgICAgICAgICAgaWYgeCAtIDEgbm90IGluIG51bXM6CiAgICAgICAgICAgICAgICAgeSA9IHggKyAxCiAgICAgICAgICAgICAgICAgd2hpbGUgeSBpbiBudW1zOgogICAgICAgICAgICAgICAgICAgICB5ICs9IDEKICAgICAgICAgICAgICAgICBiZXN0ID0gbWF4KGJlc3QsIHkgLSB4KQogICAgICAgICByZXR1cm4gYmVzdA==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
