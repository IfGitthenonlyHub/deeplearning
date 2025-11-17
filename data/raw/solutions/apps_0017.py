import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("ZnJvbSBzeXMgaW1wb3J0IHN0ZGluCgp0dCA9IGludChzdGRpbi5yZWFkbGluZSgpKQoKZm9yIGxvb3AgaW4gcmFuZ2UodHQpOgoKICAgIG4gPSBpbnQoc3RkaW4ucmVhZGxpbmUoKSkKICAgIGEgPSBsaXN0KG1hcChpbnQsc3RkaW4ucmVhZGxpbmUoKS5zcGxpdCgpKSkKCiAgICBsID0gWzBdICogKG4rMSkKICAgIGFucyA9IDAKCiAgICBmb3IgaiBpbiByYW5nZShuKToKICAgICAgICByID0gWzBdICogKG4rMSkKICAgICAgICBmb3IgayBpbiByYW5nZShuLTEsaiwtMSk6CiAgICAgICAgICAgIGFucyArPSBsW2Fba11dICogclthW2pdXQogICAgICAgICAgICByW2Fba11dICs9IDEKICAgICAgICBsW2Fbal1dICs9IDEKCiAgICBwcmludCAoYW5zKQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
