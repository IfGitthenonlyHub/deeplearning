import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgc21hbGxlc3RSYW5nZUlJKHNlbGYsIEE6IExpc3RbaW50XSwgSzogaW50KSAtPiBpbnQ6CiAgICAgICAgQS5zb3J0KCkKICAgICAgICByZXMgPSBBWy0xXSAtIEFbMF0KICAgICAgICBmb3IgaSBpbiByYW5nZShsZW4oQSktMSk6CiAgICAgICAgICAgIHJlcyA9IG1pbihyZXMsIG1heChBW2ldK0ssIEFbLTFdIC0gSykgLSBtaW4oQVswXSArIEssIEFbaSsxXSAtIEspKQogICAgICAgIHJldHVybiByZXM=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
