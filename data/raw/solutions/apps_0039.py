import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("dCA9IGludChpbnB1dCgpKQpmb3IgdHQgaW4gcmFuZ2UodCk6CglhLCBiLCBwID0gbWFwKGludCwgaW5wdXQoKS5zcGxpdCgpKQoJcyA9IGlucHV0KCkKCWNzID0geydBJzphLCAnQic6Yn0KCWMgPSAwCglpID0gbGVuKHMpLTEKCXdoaWxlIGkgPiAwIGFuZCBjK2NzW3NbaS0xXV0gPD0gcDoKCQkjIHByaW50KHR0LCBpKQoJCWMgKz0gY3Nbc1tpLTFdXQoJCWkgLT0gMQoJCXdoaWxlIGkgPiAwIGFuZCBzW2ktMV0gPT0gc1tpXToKCQkJaSAtPSAxCglwcmludChpKzEp").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
