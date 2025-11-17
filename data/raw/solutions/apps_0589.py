import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("dCA9IGludChpbnB1dCgpKQpmb3IgXyBpbiByYW5nZSh0KSA6CiBwYXRoID0gc3RyKGlucHV0KCkpLnNwbGl0KCcjJykKIGMgPSAwCiBqdW1wID0gMAogZm9yIGkgaW4gcGF0aCA6CiAgaWYgbGVuKGkpID4ganVtcCA6CiAgIGp1bXAgPSBsZW4oaSkKICAgYyArPSAxCiBwcmludChjKQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
