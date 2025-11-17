import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgZGVmIHNwbGl0QXJyYXkoc2VsZiwgbnVtcywgbSk6CiAgICAgICAgICIiIgogICAgICAgICA6dHlwZSBudW1zOiBMaXN0W2ludF0KICAgICAgICAgOnR5cGUgbTogaW50CiAgICAgICAgIDpydHlwZTogaW50CiAgICAgICAgICIiIgogICAgICAgICBkZWYgdmFsaWQobWlkKToKICAgICAgICAgICAgIGNudCA9IDAKICAgICAgICAgICAgIGN1cnJlbnQgPSAwCiAgICAgICAgICAgICBmb3IgbiBpbiBudW1zOgogICAgICAgICAgICAgICAgIGN1cnJlbnQgKz0gbgogICAgICAgICAgICAgICAgIGlmIGN1cnJlbnQ+bWlkOgogICAgICAgICAgICAgICAgICAgICBjbnQgKz0gMQogICAgICAgICAgICAgICAgICAgICBpZiBjbnQ+PW06CiAgICAgICAgICAgICAgICAgICAgICAgICByZXR1cm4gRmFsc2UKICAgICAgICAgICAgICAgICAgICAgY3VycmVudCA9IG4KICAgICAgICAgICAgIHJldHVybiBUcnVlCiAKICAgICAgICAgbCA9IG1heChudW1zKQogICAgICAgICBoID0gc3VtKG51bXMpCiAKICAgICAgICAgd2hpbGUgbDxoOgogICAgICAgICAgICAgbWlkID0gbCsoaC1sKS8yCiAgICAgICAgICAgICBpZiB2YWxpZChtaWQpOgogICAgICAgICAgICAgICAgIGggPSBtaWQKICAgICAgICAgICAgIGVsc2U6CiAgICAgICAgICAgICAgICAgbCA9IG1pZCsxCiAgICAgICAgIHJldHVybiBpbnQobCk=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
