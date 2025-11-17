import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Zm9yIGlyamZyIGluIHJhbmdlKGludChpbnB1dCgpKSk6CiAgICBpbnB1dCgpCiAgICBzID0gaW5wdXQoKQogICAgcmVzID0gaW50KHNbMF0gPT0gc1stMV0gPT0gJzEnKQogICAgZm9yIGkgaW4gcmFuZ2UobGVuKHMpIC0gMSk6CiAgICAgICAgcmVzICs9IGludChzW2ldID09IHNbaSArIDFdID09ICcxJykKICAgIHByaW50KHJlcyk=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
