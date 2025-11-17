import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("ZGVmIHNvbHZlKCk6CiBuLGs9bWFwKGludCxpbnB1dCgpLnNwbGl0KCkpCiB3PWxpc3QobWFwKGludCxpbnB1dCgpLnNwbGl0KCkpKQogaWYgazw9bi8vMjoKICB3LnNvcnQoKQogZWxzZToKICB3LnNvcnQocmV2ZXJzZT1UcnVlKQogcHJpbnQoYWJzKHN1bSh3W2s6XSktc3VtKHdbOmtdKSkpCgp0PWludChpbnB1dCgpKQp3aGlsZSB0Ogogc29sdmUoKQogdC09MQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
