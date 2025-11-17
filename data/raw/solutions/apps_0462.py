import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgY291bnRTZXJ2ZXJzKHNlbGYsIGdyaWQ6IExpc3RbTGlzdFtpbnRdXSkgLT4gaW50OgogICAgICAgIGZvciBpLHJvdyBpbiBlbnVtZXJhdGUoZ3JpZCk6CiAgICAgICAgICAgIGlmIHJvdy5jb3VudCgxKT4xOgogICAgICAgICAgICAgICAgZm9yIGosdmFsIGluIGVudW1lcmF0ZShyb3cpOgogICAgICAgICAgICAgICAgICAgIGlmIHZhbD09MToKICAgICAgICAgICAgICAgICAgICAgICAgZ3JpZFtpXVtqXT0yCiAgICAgICAgZm9yIGosY29sIGluIGVudW1lcmF0ZSh6aXAoKmdyaWQpKToKICAgICAgICAgICAgaWYgY29sLmNvdW50KDEpK2NvbC5jb3VudCgyKT4xOgogICAgICAgICAgICAgICAgZm9yIGksdmFsIGluIGVudW1lcmF0ZShjb2wpOgogICAgICAgICAgICAgICAgICAgIGlmIHZhbD09MToKICAgICAgICAgICAgICAgICAgICAgICAgZ3JpZFtpXVtqXT0yCiAgICAgICAgcmV0dXJuIHN1bSgxIGZvciByb3cgaW4gZ3JpZCBmb3IgdmFsIGluIHJvdyBpZiB2YWw9PTIp").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
