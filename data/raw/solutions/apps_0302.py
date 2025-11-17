import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgZGVmIHZhbGlkU3F1YXJlKHNlbGYsIHAxLCBwMiwgcDMsIHA0KToKICAgICAgICAgIiIiCiAgICAgICAgIDp0eXBlIHAxOiBMaXN0W2ludF0KICAgICAgICAgOnR5cGUgcDI6IExpc3RbaW50XQogICAgICAgICA6dHlwZSBwMzogTGlzdFtpbnRdCiAgICAgICAgIDp0eXBlIHA0OiBMaXN0W2ludF0KICAgICAgICAgOnJ0eXBlOiBib29sCiAgICAgICAgICIiIgogICAgICAgICBwcyA9IHNvcnRlZChbcDEscDIscDMscDRdKQogICAgICAgICByZXR1cm4gcHNbMF1bMF0rcHNbM11bMF09PXBzWzFdWzBdK3BzWzJdWzBdIGFuZCBwc1swXVsxXStwc1szXVsxXT09cHNbMV1bMV0rcHNbMl1bMV0gYW5kIHBzWzJdWzBdLXBzWzFdWzBdPT1hYnMocHNbM11bMV0tcHNbMF1bMV0pIGFuZCBub3QgcHNbMF09PXBzWzFd").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
