import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbWluS0JpdEZsaXBzKHNlbGYsIEE6IExpc3RbaW50XSwgSzogaW50KSAtPiBpbnQ6CiAgICAgICAgY250PTAKICAgICAgICBkcT1jb2xsZWN0aW9ucy5kZXF1ZSgpCiAgICAgICAgZm9yIGkgaW4gcmFuZ2UobGVuKEEpKToKICAgICAgICAgICAgaWYgQVtpXT09KDEgaWYgbGVuKGRxKSUyIGVsc2UgMCk6CiAgICAgICAgICAgICAgICBjbnQrPTEKICAgICAgICAgICAgICAgIGRxLmFwcGVuZChpK0stMSkKICAgICAgICAgICAgaWYgZHEgYW5kIGRxWzBdPT1pOgogICAgICAgICAgICAgICAgZHEucG9wbGVmdCgpCiAgICAgICAgcmV0dXJuIC0xIGlmIGxlbihkcSkgZWxzZSBjbnQ=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
