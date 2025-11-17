import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgcHJpbWVQYWxpbmRyb21lKHNlbGYsIE46IGludCkgLT4gaW50OgogICAgICAgIGRlZiBjaGVja19wKG4pOgogICAgICAgICAgICByZXR1cm4gbj4xIGFuZCBhbGwobiVkIGZvciBkIGluIHJhbmdlKDIsIGludChuKiowLjUpKzEpKQogICAgICAgIHdoaWxlIFRydWU6CiAgICAgICAgICAgIGlmIHN0cihOKT09c3RyKE4pWzo6LTFdIGFuZCBjaGVja19wKE4pOgogICAgICAgICAgICAgICAgcmV0dXJuIE4KICAgICAgICAgICAgTis9MQogICAgICAgICAgICBpZiAxMCoqOD5OPjEwKio3OgogICAgICAgICAgICAgICAgTj0xMCoqOA==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
