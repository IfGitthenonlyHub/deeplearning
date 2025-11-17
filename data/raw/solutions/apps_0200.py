import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgZmluZE1pbkZpYm9uYWNjaU51bWJlcnMoc2VsZiwgazogaW50KSAtPiBpbnQ6CiAgICAgICAgYSA9IGIgPSAxCiAgICAgICAgZmlibyA9IFthLGJdCiAgICAgIAogICAgICAgIHJlcyA9IDAKICAgICAgICB3aGlsZSBhICsgYiA8PSBrOgogICAgICAgICAgICBmaWJvLmFwcGVuZChhICsgYikKICAgICAgICAgICAgYSwgYiA9IGIsIGErYgogICAgICAgIGZvciBpIGluIGZpYm9bOjotMV06CiAgICAgICAgICAgIGlmIGsgPj0gaToKICAgICAgICAgICAgICAgIGsgLT0gaQogICAgICAgICAgICAgICAgcmVzICs9MQogICAgICAgIHJldHVybiByZXM=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
