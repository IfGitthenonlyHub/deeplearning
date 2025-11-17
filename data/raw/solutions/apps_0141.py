import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbnVtUmVzY3VlQm9hdHMoc2VsZiwgcGVvcGxlOiBMaXN0W2ludF0sIGxpbWl0OiBpbnQpIC0+IGludDoKICAgICAgICBwZW9wbGUuc29ydCgpCiAgICAgICAgaSxqPTAsbGVuKHBlb3BsZSktMQogICAgICAgIHJlcz0wCiAgICAgICAgd2hpbGUgaTw9ajoKICAgICAgICAgICAgcmVzKz0xCiAgICAgICAgICAgIGlmIHBlb3BsZVtpXStwZW9wbGVbal08PWxpbWl0OgogICAgICAgICAgICAgICAgaSs9MQogICAgICAgICAgICBqLT0xCiAgICAgICAgcmV0dXJuIHJlcw==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
