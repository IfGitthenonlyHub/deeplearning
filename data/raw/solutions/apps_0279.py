import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgZGVmIGdldFBlcm11dGF0aW9uKHNlbGYsIG4sIGspOgogICAgICAgICAiIiIKICAgICAgICAgOnR5cGUgbjogaW50CiAgICAgICAgIDp0eXBlIGs6IGludAogICAgICAgICA6cnR5cGU6IHN0cgogICAgICAgICAiIiIKICAgICAgICAgbnVtcyA9IGxpc3QoIjEyMzQ1Njc4OSIpCiAgICAgICAgIGsgLT0gMQogICAgICAgICBmYWN0b3IgPSAxCiAgICAgICAgIGZvciBpIGluIHJhbmdlKDEsIG4pOgogICAgICAgICAgICAgZmFjdG9yICo9IGkKICAgICAgICAgcmVzID0gW10KICAgICAgICAgZm9yIGkgaW4gcmV2ZXJzZWQobGlzdChyYW5nZShuKSkpOgogICAgICAgICAgICAgcmVzLmFwcGVuZChudW1zW2svL2ZhY3Rvcl0pCiAgICAgICAgICAgICBudW1zLnJlbW92ZShudW1zW2svL2ZhY3Rvcl0pCiAgICAgICAgICAgICBpZiBpOgogICAgICAgICAgICAgICAgIGsgJT0gZmFjdG9yCiAgICAgICAgICAgICAgICAgZmFjdG9yIC8vPSBpCiAgICAgICAgIHJldHVybiAiIi5qb2luKHJlcyk=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
