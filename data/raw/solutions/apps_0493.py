import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgZGVmIGZpbmRUYXJnZXRTdW1XYXlzKHNlbGYsIG51bXMsIFMpOgogICAgICAgICBzdW1fID0gc3VtKG51bXMpCiAgICAgICAgIGlmIFMgPiBzdW1fOiByZXR1cm4gMAogICAgICAgICB0YXJnZXQgPSBzdW1fIC0gUwogICAgICAgICBpZiB0YXJnZXQgJSAyOiByZXR1cm4gMAogICAgICAgICB0YXJnZXQgPSB0YXJnZXQgLy8gMgogCiAgICAgICAgIGRwID0gWzFdICsgWzBdICogdGFyZ2V0CiAgICAgICAgIGZvciBuIGluIG51bXM6CiAgICAgICAgICAgICBpID0gdGFyZ2V0ICAKICAgICAgICAgICAgIHdoaWxlKGk+PW4pOiAgCiAgICAgICAgICAgICAgICAgZHBbaV0gKz0gZHBbaS1uXSAgCiAgICAgICAgICAgICAgICAgaSAtPSAxIAogICAgICAgICByZXR1cm4gZHBbdGFyZ2V0XQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
