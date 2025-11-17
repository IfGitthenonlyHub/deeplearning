import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Zm9yIF8gaW4gcmFuZ2UoaW50KGlucHV0KCkpKToKCWEsYiA9IGxpc3QobWFwKGludCwgaW5wdXQoKS5zcGxpdCgpKSkKCXMgPSBpbnB1dCgpCgljb3N0ID0gMAoJcm93Y29zdCA9IGEKCWFtY2hhaW4gPSBGYWxzZQoJZm9yIGMgaW4gczoKCQlpZiBjID09ICcxJzoKCQkJaWYgbm90IGFtY2hhaW4gYW5kIHJvd2Nvc3Q6CgkJCQlhbWNoYWluID0gVHJ1ZQoJCQkJY29zdCArPSBtaW4ocm93Y29zdCwgYSkKCQllbHNlOgoJCQlpZiBhbWNoYWluOgoJCQkJYW1jaGFpbiA9IEZhbHNlCgkJCQlyb3djb3N0ID0gYgoJCQllbHNlOgoJCQkJcm93Y29zdCArPSBiCglwcmludChjb3N0KQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
