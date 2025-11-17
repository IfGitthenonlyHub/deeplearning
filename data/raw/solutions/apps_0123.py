import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbnVtTXVzaWNQbGF5bGlzdHMoc2VsZiwgTjogaW50LCBMOiBpbnQsIEs6IGludCkgLT4gaW50OgogICAgICAgIAogICAgICAgIEBscnVfY2FjaGUoTm9uZSkKICAgICAgICBkZWYgZHAoaSwgaik6CiAgICAgICAgICAgIGlmIGkgPT0gMDoKICAgICAgICAgICAgICAgIHJldHVybiBqID09IDAKICAgICAgICAgICAgCiAgICAgICAgICAgIHJldHVybiAoZHAoaS0xLCBqKSAqIG1heCgwLCBqIC0gSykgKyBkcChpLTEsIGotMSkgKiAoTiAtIGogKyAxKSkgJSAoMTAqKjkgKyA3KQogICAgICAgIAogICAgICAgIHJldHVybiBkcChMLCBOKQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
