import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("aW1wb3J0IHN5cwppbnB1dCA9IHN5cy5zdGRpbi5yZWFkbGluZQpJID0gbGFtYmRhIDogbGlzdChtYXAoaW50LGlucHV0KCkuc3BsaXQoKSkpCgp0LD1JKCkKZm9yIGkgaW4gcmFuZ2UodCk6CgluLD1JKCkKCWE9SSgpCglsPUkoKQoJYXI9W2FbaV0gZm9yIGkgaW4gcmFuZ2UobikgaWYgbFtpXT09MF0KCWFyLnNvcnQocmV2ZXJzZT1UcnVlKQoJeD0wCglmb3IgaSBpbiByYW5nZShuKToKCQlpZiBsW2ldPT0wOgoJCQlhW2ldPWFyW3hdCgkJCXgrPTEKCXByaW50KCphKQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
