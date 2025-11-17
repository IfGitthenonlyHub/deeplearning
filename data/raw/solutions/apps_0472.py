import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgY2FuUmVhY2goc2VsZiwgYXJyOiBMaXN0W2ludF0sIHN0YXJ0OiBpbnQpIC0+IGJvb2w6CiAgICAgICAgaWYgMCA8PSBzdGFydCA8IGxlbihhcnIpIGFuZCBhcnJbc3RhcnRdID49IDA6CiAgICAgICAgICAgIGlmIGFycltzdGFydF0gPT0gMDoKICAgICAgICAgICAgICAgIHJldHVybiBUcnVlCgogICAgICAgICAgICBhcnJbc3RhcnRdID0gLWFycltzdGFydF0KICAgICAgICAgICAgcmV0dXJuIHNlbGYuY2FuUmVhY2goYXJyLCBzdGFydCthcnJbc3RhcnRdKSBvciBzZWxmLmNhblJlYWNoKGFyciwgc3RhcnQtYXJyW3N0YXJ0XSkKCiAgICAgICAgcmV0dXJuIEZhbHNl").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
