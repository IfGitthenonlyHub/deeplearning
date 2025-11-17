import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgYnJlYWtQYWxpbmRyb21lKHNlbGYsIHM6IHN0cikgLT4gc3RyOgogICAgICAgIGZvciBpIGluIHJhbmdlKGxlbihzKS8vMik6CiAgICAgICAgICAgIGlmIHNbaV0hPSdhJzoKICAgICAgICAgICAgICAgIHJldHVybiBzWzppXSArICdhJyArIHNbaSsxOl0KICAgICAgICBpZiBzWzotMV06CiAgICAgICAgICAgIHJldHVybiBzWzotMV0gKyAnYicKICAgICAgICBlbHNlOgogICAgICAgICAgICByZXR1cm4gJyc=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
