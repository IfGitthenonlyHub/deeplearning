import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbWF4UGVyZm9ybWFuY2Uoc2VsZiwgbiwgc3BlZWQsIGVmZmljaWVuY3ksIGspOgogICAgICAgIGggPSBbXQogICAgICAgIHJlcyA9IHNTdW0gPSAwCiAgICAgICAgZm9yIGUsIHMgaW4gc29ydGVkKHppcChlZmZpY2llbmN5LCBzcGVlZCksIHJldmVyc2U9MSk6CiAgICAgICAgICAgIGhlYXBxLmhlYXBwdXNoKGgsIHMpCiAgICAgICAgICAgIHNTdW0gKz0gcwogICAgICAgICAgICBpZiBsZW4oaCkgPiBrOgogICAgICAgICAgICAgICAgc1N1bSAtPSBoZWFwcS5oZWFwcG9wKGgpCiAgICAgICAgICAgIHJlcyA9IG1heChyZXMsIHNTdW0gKiBlKQogICAgICAgIHJldHVybiByZXMgJSAoMTAqKjkgKyA3KQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
