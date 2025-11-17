import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Zm9yIF8gaW4gcmFuZ2UoaW50KGlucHV0KCkpKToKCW49aW50KGlucHV0KCkpCglhPWxpc3QobWFwKGludCxpbnB1dCgpLnNwbGl0KCkpKQoJI24saz1tYXAoaW50LGlucHV0KCkuc3BsaXQoKSkKCXllcz0wIAoJZm9yIGkgaW4gcmFuZ2UoMSxuLTEpOgoJCWlmKGFbaV0+YVtpLTFdIGFuZCBhW2ldPmFbaSsxXSk6CgkJCXByaW50KCdZRVMnKQoJCQlwcmludChpLTErMSxpKzEsaSsyKQoJCQl5ZXM9MQoJCQlicmVhayAKCWlmKHllcz09MCk6CgkJcHJpbnQoJ05PJyk=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
