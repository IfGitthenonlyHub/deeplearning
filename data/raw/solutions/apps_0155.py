import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbWF4SnVtcHMoc2VsZiwgYXJyOiBMaXN0W2ludF0sIGQ6IGludCkgLT4gaW50OgogICAgICAgICN0b3AtZG93biBkcAogICAgICAgIHJlcyA9IFsxXSAqIGxlbihhcnIpCiAgICAgICAgZm9yIGEsIGkgaW4gc29ydGVkKFthLCBpXSBmb3IgaSwgYSBpbiBlbnVtZXJhdGUoYXJyKSk6CiAgICAgICAgICAgIGZvciBkaSBpbiBbLTEsIDFdOgogICAgICAgICAgICAgICAgZm9yIGogaW4gcmFuZ2UoaSArIGRpLCBpICsgZCAqIGRpICsgZGksIGRpKToKICAgICAgICAgICAgICAgICAgICBpZiBub3QgKDAgPD0gaiA8IGxlbihhcnIpIGFuZCBhcnJbal0gPCBhcnJbaV0pOiBicmVhawogICAgICAgICAgICAgICAgICAgIHJlc1tpXSA9IG1heChyZXNbaV0sIDEgKyByZXNbal0pCiAgICAgICAgcmV0dXJuIG1heChyZXMp").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
