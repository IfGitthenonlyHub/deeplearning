import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgc2NvcmVPZlBhcmVudGhlc2VzKHNlbGYsIFM6IHN0cikgLT4gaW50OgogICAgICAgIGFucywgdmFsID0gMCwgMQogICAgICAgIGZvciBpIGluIHJhbmdlKGxlbihTKSAtIDEpOgogICAgICAgICAgICBpZiBTW2k6IGkrMl0gPT0gJygoJzogdmFsICo9IDIKICAgICAgICAgICAgaWYgU1tpOiBpKzJdID09ICcoKSc6IGFucyArPSB2YWwKICAgICAgICAgICAgaWYgU1tpOiBpKzJdID09ICcpKSc6IHZhbCAvLz0gMgogICAgICAgIHJldHVybiBhbnM=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
