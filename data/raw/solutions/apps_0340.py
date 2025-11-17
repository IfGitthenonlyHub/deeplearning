import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgZGVmIHNpbXBsaWZ5UGF0aChzZWxmLCBwYXRoKToKICAgICAgICAgIiIiCiAgICAgICAgIDp0eXBlIHBhdGg6IHN0cgogICAgICAgICA6cnR5cGU6IHN0cgogICAgICAgICAiIiIKICAgICAgICAgc3RhY2sgPSBbXQogICAgICAgICBmb3IgcCBpbiBwYXRoLnNwbGl0KCIvIik6CiAgICAgICAgICAgICBpZiBwID09ICIuLiI6CiAgICAgICAgICAgICAgICAgaWYgc3RhY2s6CiAgICAgICAgICAgICAgICAgICAgIHN0YWNrLnBvcCgpCiAgICAgICAgICAgICBlbGlmIHAgYW5kIHAgIT0gJy4nOgogICAgICAgICAgICAgICAgIHN0YWNrLmFwcGVuZChwKQogICAgICAgICByZXR1cm4gIi8iICsgIi8iLmpvaW4oc3RhY2sp").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
