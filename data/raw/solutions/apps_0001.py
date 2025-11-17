import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("cSA9IGludChpbnB1dCgpKQoKZm9yIGkgaW4gcmFuZ2UocSk6CiAgICBuLCBtLCBrID0gbWFwKGludCwgaW5wdXQoKS5zcGxpdCgpKQogICAgcCA9IG1pbihtLCBuKQogICAgciA9IG1heChuLCBtKSAtIHAKICAgIGlmIChwK3IpID4gazoKICAgICAgICBwcmludCgtMSkKICAgIGVsaWYgciAlIDIgPT0gMToKICAgICAgICBwcmludChrIC0gMSkKICAgIGVsaWYgKGsgLSBwKSAlIDIgPT0gMDoKICAgICAgICBwcmludChrKQogICAgZWxzZToKICAgICAgICBwcmludChrIC0gMik=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
