import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("dD1pbnQoaW5wdXQoKSkKZm9yIGkgaW4gcmFuZ2UodCk6CiAgICBuPWludChpbnB1dCgpKQogICAgYT1baW50KHgpIGZvciB4IGluIGlucHV0KCkuc3BsaXQoKV0KICAgIGI9WzBdICogbgogICAgbT0wCiAgICBjPXNldChyYW5nZSgxLCBuKzEpKQogICAgZm9yIGkgaW4gcmFuZ2Uobik6CiAgICAgICAgaWYgYVtpXSA+IG06CiAgICAgICAgICAgIGJbaV0gPSBhW2ldCiAgICAgICAgICAgIG0gPSBhW2ldCiAgICAgICAgICAgIGMuZGlzY2FyZChhW2ldKQogICAgYz1zb3J0ZWQoYykKICAgIGo9MAogICAgZm9yIGkgaW4gcmFuZ2Uobik6CiAgICAgICAgaWYgYltpXSA9PSAwOgogICAgICAgICAgICBiW2ldID0gY1tqXQogICAgICAgICAgICBqKz0xCiAgICAgICAgICAgIGlmIGJbaV0gPiBhW2ldOgogICAgICAgICAgICAgICAgcHJpbnQoLTEpCiAgICAgICAgICAgICAgICBicmVhawogICAgZWxzZToKICAgICAgICBwcmludCgqYik=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
