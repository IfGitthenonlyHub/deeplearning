import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbWF4V2lkdGhSYW1wKHNlbGYsIGE6IExpc3RbaW50XSkgLT4gaW50OgogICAgICAgIHNpcyA9IHNvcnRlZChsaXN0KHJhbmdlKGxlbihhKSkpLCBrZXk9YS5fX2dldGl0ZW1fXykKICAgICAgICByZXR1cm4gbWF4KGkgLSBtIGZvciBtLCBpIGluIHppcChpdGVydG9vbHMuYWNjdW11bGF0ZShzaXMsIG1pbiksIHNpcykp").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
