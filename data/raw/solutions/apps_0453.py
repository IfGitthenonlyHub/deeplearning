import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbWluQ29zdChzZWxmLCBBLCBjb3N0LCBtLCBuLCB0YXJnZXQpOgogICAgICAgIGRwLCBkcDIgPSB7KDAsIDApOiAwfSwge30KICAgICAgICBmb3IgaSwgYSBpbiBlbnVtZXJhdGUoQSk6CiAgICAgICAgICAgIGZvciBjaiBpbiAocmFuZ2UoMSwgbiArIDEpIGlmIGEgPT0gMCBlbHNlIFthXSk6CiAgICAgICAgICAgICAgICBmb3IgY2ksIGIgaW4gZHA6CiAgICAgICAgICAgICAgICAgICAgYjIgPSBiICsgKGNpICE9IGNqKQogICAgICAgICAgICAgICAgICAgIGlmIGIyID4gdGFyZ2V0OiBjb250aW51ZQogICAgICAgICAgICAgICAgICAgIGRwMltjaiwgYjJdID0gbWluKGRwMi5nZXQoKGNqLGIyKSwgZmxvYXQoJ2luZicpKSwgZHBbY2ksIGJdICsgKGNvc3RbaV1bY2ogLSAxXSBpZiBjaiAhPSBhIGVsc2UgMCkpCiAgICAgICAgICAgIGRwLCBkcDIgPSBkcDIsIHt9CiAgICAgICAgcmV0dXJuIG1pbihbZHBbYywgYl0gZm9yIGMsIGIgaW4gZHAgaWYgYiA9PSB0YXJnZXRdIG9yIFstMV0p").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
