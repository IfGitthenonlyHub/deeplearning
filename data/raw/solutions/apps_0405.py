import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbmV3MjFHYW1lKHNlbGYsIE46IGludCwgSzogaW50LCBXOiBpbnQpIC0+IGZsb2F0OgogICAgICAgIGRwID0gWzBdICogKE4gKyBXKQogICAgICAgIGZvciBpIGluIHJhbmdlKEssIE4gKyAxKToKICAgICAgICAgICAgZHBbaV0gPSAxCiAgICAgICAgCiAgICAgICAgUyA9IG1pbihXLCBOIC0gSyArIDEpCiAgICAgICAgZm9yIGkgaW4gcmFuZ2UoSyAtIDEsIC0xLCAtMSk6CiAgICAgICAgICAgIGRwW2ldID0gUyAvIFcKICAgICAgICAgICAgUyArPSBkcFtpXSAtIGRwW2kgKyBXXQogICAgICAgIHJldHVybiBkcFswXQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
