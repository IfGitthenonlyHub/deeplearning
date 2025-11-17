import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbnVtYmVyT2ZBcnJheXMoc2VsZiwgczogc3RyLCBrOiBpbnQpIC0+IGludDoKICAgICAgICBNT0QgPSAxMCAqKiA5ICsgNwogICAgICAgIG4gPSBsZW4ocykKICAgICAgICBAbHJ1X2NhY2hlKE5vbmUpCiAgICAgICAgZGVmIGRwKGkpOgogICAgICAgICAgICBpZiBpID09IG46CiAgICAgICAgICAgICAgICByZXR1cm4gMQogICAgICAgICAgICBpZiBzW2ldID09ICcwJzoKICAgICAgICAgICAgICAgIHJldHVybiAwCiAgICAgICAgICAgIG51bSA9IDAKICAgICAgICAgICAgYW5zID0gMAogICAgICAgICAgICBmb3IgaiBpbiByYW5nZShpLCBuKToKICAgICAgICAgICAgICAgIG51bSA9IG51bSAqIDEwICsgb3JkKHNbal0pIC0gb3JkKCcwJykKICAgICAgICAgICAgICAgIGlmIG51bSA+IGs6CiAgICAgICAgICAgICAgICAgICAgYnJlYWsKICAgICAgICAgICAgICAgIGFucyArPSBkcChqKzEpCiAgICAgICAgICAgIHJldHVybiBhbnMgJSBNT0QKICAgICAgICAKICAgICAgICByZXR1cm4gZHAoMCk=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
