import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgYXJyYW5nZVdvcmRzKHNlbGYsIHRleHQ6IHN0cikgLT4gc3RyOgogICAgICAgIGlmIG5vdCB0ZXh0OgogICAgICAgICAgICByZXR1cm4gdGV4dAogICAgICAgIAogICAgICAgIHdvcmRzID0gdGV4dC5sb3dlcigpLnNwbGl0KCcgJykKICAgICAgICAKICAgICAgICB3b3JkcyA9IHNvcnRlZCh3b3Jkcywga2V5ID0gbGFtYmRhIHg6IGxlbih4KSkKICAgICAgICB3b3Jkc1swXSA9IHdvcmRzWzBdWzBdLnVwcGVyKCkgKyB3b3Jkc1swXVsxOl0KICAgICAgICAKICAgICAgICByZXR1cm4gJyAnLmpvaW4od29yZHMp").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
