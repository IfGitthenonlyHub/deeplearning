import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgY2FyRmxlZXQoc2VsZiwgdGFyZ2V0OiBpbnQsIHBvc2l0aW9uOiBMaXN0W2ludF0sIHNwZWVkOiBMaXN0W2ludF0pIC0+IGludDoKICAgICAgICB0aW1lID0gWyh0YXJnZXQgLSBwKSAvIHMgZm9yIHAsIHMgaW4gc29ydGVkKHppcChwb3NpdGlvbiwgc3BlZWQpLCBrZXk9bGFtYmRhIHg6IHhbMF0pXQogICAgICAgIGZsZWV0cyA9IDAKICAgICAgICBsYXN0X2Fycml2ZSA9IDAKICAgICAgICBmb3IgdCBpbiB0aW1lWzo6LTFdOgogICAgICAgICAgICBpZiB0ID4gbGFzdF9hcnJpdmU6CiAgICAgICAgICAgICAgICBsYXN0X2Fycml2ZSA9IHQKICAgICAgICAgICAgICAgIGZsZWV0cyArPSAxCiAgICAgICAgcmV0dXJuIGZsZWV0cw==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
