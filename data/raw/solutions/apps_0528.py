import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("VCA9IGludChpbnB1dCgpKQpmb3IgXyBpbiByYW5nZShUKToKIG4sIGwgPSBtYXAoaW50LGlucHV0KCkuc3BsaXQoKSkKIGlmIG4gPT0gMToKICBwcmludChsKQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
