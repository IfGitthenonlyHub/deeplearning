import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgZmluZFRoZUxvbmdlc3RTdWJzdHJpbmcoc2VsZiwgcyk6CiAgICAgICAgc2VlbiA9IHswOiAtMX0KICAgICAgICByZXMgPSBjdXIgPSAwCiAgICAgICAgZm9yIGksIGMgaW4gZW51bWVyYXRlKHMpOgogICAgICAgICAgICBjdXIgXj0gMSA8PCAoJ2FlaW91Jy5maW5kKGMpICsgMSkgPj4gMQogICAgICAgICAgICBzZWVuLnNldGRlZmF1bHQoY3VyLCBpKQogICAgICAgICAgICByZXMgPSBtYXgocmVzLCBpIC0gc2VlbltjdXJdKQogICAgICAgIHJldHVybiByZXM=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
