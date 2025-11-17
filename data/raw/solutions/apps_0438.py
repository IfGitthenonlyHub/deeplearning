import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgZmluZExhdGVzdFN0ZXAoc2VsZiwgYXJyOiBMaXN0W2ludF0sIG06IGludCkgLT4gaW50OgogICAgICAgIGEsYixzLHQ9WzBdKihsZW4oYXJyKSsyKSxbMF0qKGxlbihhcnIpKzEpLC0xLDAKICAgICAgICBmb3IgcCxpIGluIGVudW1lcmF0ZShhcnIsMSk6CiAgICAgICAgICAgIGosaz1hW2ktMV0sYVtpKzFdCiAgICAgICAgICAgIGFbaV09YVtpLWpdPWFbaStrXT1qK2srMQogICAgICAgICAgICBpZiBhW2ldPT1tOiB0Kz0xCiAgICAgICAgICAgIGlmIGo9PW06IHQtPTEKICAgICAgICAgICAgaWYgaz09bTogdC09MQogICAgICAgICAgICBpZiB0OiBzPXAKICAgICAgICByZXR1cm4gcw==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
