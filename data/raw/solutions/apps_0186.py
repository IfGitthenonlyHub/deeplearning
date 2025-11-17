import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbGFyZ2VzdE51bWJlcihzZWxmLCBjb3N0LCB0YXJnZXQpOgogICAgICAgIGRwID0gWzBdICsgWy0xXSAqICh0YXJnZXQgKyA1MDAwKQogICAgICAgIGZvciB0IGluIHJhbmdlKDEsIHRhcmdldCArIDEpOgogICAgICAgICAgICBkcFt0XSA9IG1heChkcFt0IC0gY10gKiAxMCArIGkgKyAxIGZvciBpLCBjIGluIGVudW1lcmF0ZShjb3N0KSkKICAgICAgICByZXR1cm4gc3RyKG1heChkcFt0XSwgMCkp").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
