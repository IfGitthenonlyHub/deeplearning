import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgb3JkZXJseVF1ZXVlKHNlbGYsIFM6IHN0ciwgSzogaW50KSAtPiBzdHI6CiAgICAgICAgaWYgSz09MToKICAgICAgICAgICAgdG1wID0gUwogICAgICAgICAgICBmb3IgaSBpbiByYW5nZShsZW4oUykpOgogICAgICAgICAgICAgICAgUyA9IFNbMTpdICsgc3RyKFNbMF0pCiAgICAgICAgICAgICAgICBpZiBTPHRtcDoKICAgICAgICAgICAgICAgICAgICB0bXAgPSBTCiAgICAgICAgICAgIHJldHVybiB0bXAKICAgICAgICBlbHNlOgogICAgICAgICAgICByZXR1cm4gJycuam9pbihzb3J0ZWQoUykp").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
