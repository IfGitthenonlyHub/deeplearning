import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgcmV2ZXJzZVBhcmVudGhlc2VzKHNlbGYsIHM6IHN0cikgLT4gc3RyOgogICAgICAgIHN0YWNrID0gWycnXQogICAgICAgIGZvciBjIGluIHM6CiAgICAgICAgICAgIGlmIGMgPT0gJygnOgogICAgICAgICAgICAgICAgc3RhY2suYXBwZW5kKCcnKQogICAgICAgICAgICBlbGlmIGMgPT0gJyknOgogICAgICAgICAgICAgICAgd29yZCA9IHN0YWNrLnBvcCgpWzo6LTFdCiAgICAgICAgICAgICAgICBzdGFja1stMV0gKz0gd29yZAogICAgICAgICAgICBlbHNlOgogICAgICAgICAgICAgICAgc3RhY2tbLTFdICs9IGMKICAgICAgICByZXR1cm4gJycuam9pbihzdGFjayk=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
