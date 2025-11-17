import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("dD1pbnQoaW5wdXQoKSkKZm9yIF8gaW4gcmFuZ2UodCk6CiAgICBzPWlucHV0KCkKICAgIHg9IiIKICAgIGk9MAogICAgYW5zPTAKICAgIHdoaWxlIGk8bGVuKHMpOgogICAgICAgIHg9c1tpXQogICAgICAgIGM9MQogICAgICAgIGkrPTEKICAgICAgICB3aGlsZSBpPGxlbihzKSBhbmQgc1tpXT09eDoKICAgICAgICAgICAgaSs9MQogICAgICAgICAgICBjKz0xCiAgICAgICAgaWYgYz09MToKICAgICAgICAgICAgYW5zKz04CiAgICAgICAgZWxzZToKICAgICAgICAgICAgYW5zKz00MAogICAgbT04KmxlbihzKQogICAgcHJpbnQobS1hbnMp").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
