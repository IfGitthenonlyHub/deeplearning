import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbWluRGVsZXRpb25TaXplKHNlbGYsIEEpOgogICAgICAgIFcgPSBsZW4oQVswXSkKICAgICAgICBkcCA9IFsxXSAqIFcKICAgICAgICBmb3IgaiBpbiByYW5nZSgxLCBXKToKICAgICAgICAgICAgZm9yIGkgaW4gcmFuZ2Uoaik6CiAgICAgICAgICAgICAgICBpZiBhbGwocm93W2ldIDw9IHJvd1tqXSBmb3Igcm93IGluIEEpOgogICAgICAgICAgICAgICAgICAgIGRwW2pdID0gbWF4KGRwW2ldKzEsIGRwW2pdKQogICAgICAgIHJldHVybiBXIC0gbWF4KGRwKQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
