import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbWF4U3VtKHNlbGYsIG51bXMxOiBMaXN0W2ludF0sIG51bXMyOiBMaXN0W2ludF0pIC0+IGludDoKICAgICAgICBsMSxsMj1sZW4obnVtczEpLGxlbihudW1zMikKICAgICAgICBnPWRlZmF1bHRkaWN0KHNldCkKICAgICAgICBmb3IgaSBpbiByYW5nZSgxLGwxKTogZ1tudW1zMVtpLTFdXS5hZGQobnVtczFbaV0pCiAgICAgICAgZm9yIGkgaW4gcmFuZ2UoMSxsMik6IGdbbnVtczJbaS0xXV0uYWRkKG51bXMyW2ldKQogICAgICAgIEBscnVfY2FjaGUoTm9uZSkKICAgICAgICBkZWYgZGZzKG4pOgogICAgICAgICAgICB4PTAKICAgICAgICAgICAgZm9yIGkgaW4gZ1tuXTogeD1tYXgoeCxkZnMoaSkpCiAgICAgICAgICAgIHJldHVybiBuK3gKICAgICAgICByZXM9bWF4KGRmcyhudW1zMVswXSksZGZzKG51bXMyWzBdKSkKICAgICAgICByZXR1cm4gcmVzJTEwMDAwMDAwMDc=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
