import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbWluY29zdFRvSGlyZVdvcmtlcnMoc2VsZiwgcXVhbGl0eSwgd2FnZSwgSyk6CiAgICAgICAgd29ya2VycyA9IHNvcnRlZChbZmxvYXQodykgLyBxLCBxXSBmb3IgdywgcSBpbiB6aXAod2FnZSwgcXVhbGl0eSkpCiAgICAgICAgcmVzID0gZmxvYXQoJ2luZicpCiAgICAgICAgcXN1bSA9IDAKICAgICAgICBoZWFwID0gW10KICAgICAgICBmb3IgciwgcSBpbiB3b3JrZXJzOgogICAgICAgICAgICBoZWFwcS5oZWFwcHVzaChoZWFwLCAtcSkKICAgICAgICAgICAgcXN1bSArPSBxCiAgICAgICAgICAgIGlmIGxlbihoZWFwKSA+IEs6IHFzdW0gKz0gaGVhcHEuaGVhcHBvcChoZWFwKQogICAgICAgICAgICBpZiBsZW4oaGVhcCkgPT0gSzogcmVzID0gbWluKHJlcywgcXN1bSAqIHIpCiAgICAgICAgcmV0dXJuIHJlcw==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
