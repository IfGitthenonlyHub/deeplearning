import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("JycnaW5wdXQKNAowMTEwCjAxMDEKMDAwMDEwMDAKMDAwMTAwMAonJycKZm9yIHRlc3QgaW4gcmFuZ2UoaW50KGlucHV0KCkpKToKCXMgPSBpbnB1dCgpCglhbnMgPSAwCglmb3IgbCBpbiByYW5nZSgxLCBtaW4oMjAsIGxlbihzKSkrMSk6CgkJcCA9IDAKCQlmb3IgaSBpbiByYW5nZShsZW4ocyktbCsxKToKCQkJaWYgc1tpXT09JzAnOgoJCQkJcCArPSAxCgkJCQljb250aW51ZQoJCQl4ID0gaW50KHNbaTppK2xdLCAyKQoJCQlpZiB4Pj1sIGFuZCAoeC1sKTw9cDoKCQkJCWFucys9MQoJCQlwID0gMAoJcHJpbnQoYW5zKQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
