import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbnVtRnJpZW5kUmVxdWVzdHMoc2VsZiwgYWdlcyk6CiAgICAgICAgZGVmIHJlcXVlc3QoYSwgYik6CiAgICAgICAgICAgIHJldHVybiBub3QgKGIgPD0gMC41ICogYSArIDcgb3IgYiA+IGEgb3IgYiA+IDEwMCBhbmQgYSA8IDEwMCkKICAgICAgICBjID0gY29sbGVjdGlvbnMuQ291bnRlcihhZ2VzKQogICAgICAgIHJldHVybiBzdW0ocmVxdWVzdChhLCBiKSAqIGNbYV0gKiAoY1tiXSAtIChhID09IGIpKSBmb3IgYSBpbiBjIGZvciBiIGluIGMp").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
