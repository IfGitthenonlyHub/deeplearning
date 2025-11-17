import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgcHJvZml0YWJsZVNjaGVtZXMoc2VsZixHLCBQLCBncm91cCwgcHJvZml0KToKICAgICAgICBkcCA9IFtbMV0rWzBdKkddICsgW1swXSooRysxKSBmb3IgXyBpbiByYW5nZShQKV0KICAgICAgICBmb3IgcCwgZyBpbiB6aXAocHJvZml0LCBncm91cCk6CiAgICAgICAgICAgIGZvciBpIGluIHJhbmdlKFAsLTEsLTEpOgogICAgICAgICAgICAgICAgZm9yIGogaW4gcmFuZ2UoRy1nLC0xLC0xKToKICAgICAgICAgICAgICAgICAgICBkcFttaW4oUCxpK3ApXVtnK2pdICs9IGRwW2ldW2pdCiAgICAgICAgcmV0dXJuIChzdW0oZHBbUF0pICUgKDEwKio5KzcpKQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
