import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgY2FuVmlzaXRBbGxSb29tcyhzZWxmLCByb29tczogTGlzdFtMaXN0W2ludF1dKSAtPiBib29sOgogICAgCiAgICAgICAgcSA9IGRlcXVlKFswXSkKICAgICAgICB2aXNpdGVkID0gc2V0KFswXSkKICAgICAgICB3aGlsZSBxOgogICAgICAgICAgICByID0gcS5wb3AoKQogICAgICAgICAgICBmb3IgayBpbiByb29tc1tyXToKICAgICAgICAgICAgICAgIGlmIGsgbm90IGluIHZpc2l0ZWQ6CiAgICAgICAgICAgICAgICAgICAgdmlzaXRlZC5hZGQoaykKICAgICAgICAgICAgICAgICAgICBxLmFwcGVuZChrKQogICAgICAgICAgICAgICAgCiAgICAgICAgcmV0dXJuIGxlbih2aXNpdGVkKT09bGVuKHJvb21zKQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
