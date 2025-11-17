import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgY2FuQXJyYW5nZShzZWxmLCBhcnI6IExpc3RbaW50XSwgazogaW50KSAtPiBib29sOgogICAgICAgIGMgPSBjb2xsZWN0aW9ucy5Db3VudGVyKFthJWsgZm9yIGEgaW4gYXJyXSkKICAgICAgICByZXR1cm4gYWxsKChjW2ldID09IGNbay1pXSkgZm9yIGkgaW4gcmFuZ2UoMSwgay8vMiArIDEpKSBhbmQgKGNbMF0gJTIgPT0gMCk=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
