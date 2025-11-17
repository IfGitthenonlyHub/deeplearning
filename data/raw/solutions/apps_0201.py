import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgZnJvbSBmdW5jdG9vbHMgaW1wb3J0IGxydV9jYWNoZQogICAgIEBscnVfY2FjaGUobWF4c2l6ZT1Ob25lKQogICAgIGRlZiBudW1UcmVlcyhzZWxmLCBoaWdoLCBsb3c9MSk6CiAgICAgICAgICIiIgogICAgICAgICA6dHlwZSBuOiBpbnQKICAgICAgICAgOnJ0eXBlOiBpbnQKICAgICAgICAgIiIiCiAgICAgICAgIHJldHVybiBzdW0oc2VsZi5udW1UcmVlcyhrZXkgLSAxLCBsb3cpICogc2VsZi5udW1UcmVlcyhoaWdoLCBrZXkgKyAxKSBmb3Iga2V5IGluIHJhbmdlKGxvdywgaGlnaCArIDEpKSBvciAx").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
