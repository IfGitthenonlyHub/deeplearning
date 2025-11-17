import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("dCA9IGludChpbnB1dCgpKQoKZm9yIGsgaW4gcmFuZ2UodCk6CiAgICBuID0gaW50KGlucHV0KCkpCiAgICBhID0gc2V0KG1hcChpbnQsIGlucHV0KCkuc3BsaXQoKSkpCiAgICBmb3IgeCBpbiByYW5nZSgxLCAxMDI1KToKICAgICAgICBpZiBzZXQoeCBeIHEgZm9yIHEgaW4gYSkgPT0gYToKICAgICAgICAgICAgcHJpbnQoeCkKICAgICAgICAgICAgYnJlYWsgCiAgICBlbHNlOgogICAgICAgIHByaW50KC0xKQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
