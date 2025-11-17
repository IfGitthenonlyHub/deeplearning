import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgdW5pcXVlTGV0dGVyU3RyaW5nKHNlbGYsIHM6IHN0cikgLT4gaW50OgogICAgICAgIGluZGV4ID0ge2NoYXI6Wy0xXStbaWMgZm9yIGljLGNoYXIwIGluIGVudW1lcmF0ZShzKSBpZiBjaGFyID09IGNoYXIwXStbbGVuKHMpXSBmb3IgY2hhciBpbiBzZXQocyl9CiAgICAgICAgcmV0dXJuIHN1bShbKGluZGV4W2NoYXJdW2pqXS1pbmRleFtjaGFyXVtqai0xXSkqKGluZGV4W2NoYXJdW2pqKzFdLWluZGV4W2NoYXJdW2pqXSkgZm9yIGNoYXIgaW4gaW5kZXggZm9yIGpqIGluIHJhbmdlKDEsbGVuKGluZGV4W2NoYXJdKS0xKV0p").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
