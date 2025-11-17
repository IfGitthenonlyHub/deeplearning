import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgdmFsaWRhdGVTdGFja1NlcXVlbmNlcyhzZWxmLCBwdXNoZWQ6IExpc3RbaW50XSwgcG9wcGVkOiBMaXN0W2ludF0pIC0+IGJvb2w6CiAgICAgICAgbD1bXQogICAgICAgIGo9aT0wCiAgICAgICAgZm9yIGkgIGluIHB1c2hlZDoKICAgICAgICAgICAgbC5hcHBlbmQoaSkKICAgICAgICAgICAgd2hpbGUgbCBhbmQgcG9wcGVkIGFuZCBsWy0xXT09cG9wcGVkWzBdOgogICAgICAgICAgICAgICAgbC5wb3AoKQogICAgICAgICAgICAgICAgcG9wcGVkLnBvcCgwKQogICAgICAgIHJldHVybiBsZW4ocG9wcGVkKT09MA==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
