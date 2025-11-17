import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Zj1pbnB1dDsgZnJvbSBiaXNlY3QgaW1wb3J0IGJpc2VjdF9sZWZ0IGFzIGcsIGluc29ydCBhcyBoCmQ9e2Nocig5NytpKTpbXSBmb3IgaSBpbiByYW5nZSgyNil9CmYoKTsgcyxpPWxpc3QoZigpKSwwCmZvciBjIGluIHM6IGRbY10rPVtpXTsgaSs9MQpmb3IgXyBpbiByYW5nZShpbnQoZigpKSk6CiAgYSxiLGM9ZigpLnNwbGl0KCk7IGI9aW50KGIpLTEKICBpZiBhPicxJzogcHJpbnQoc3VtKDEgZm9yIGwgaW4gZC52YWx1ZXMoKSBpZiBnKGwsYik8bGVuKGwpIGFuZCBsW2cobCxiKV08aW50KGMpKSkKICBlbGlmIHNbYl0hPWM6IGw9ZFtzW2JdXTsgbC5wb3AoZyhsLGIpKTsgc1tiXT1jOyBoKGRbY10sYik=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
