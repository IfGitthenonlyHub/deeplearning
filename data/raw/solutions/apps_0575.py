import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Zm9yIF8gaW4gcmFuZ2UoaW50KGlucHV0KCkpKToKIHN0PWlucHV0KCkucmVwbGFjZSgiPSIsIiIpCiBpZiBub3QgbGVuKHN0KTpwcmludCgxKQogZWxzZToKICBjdT1teD0xCiAgZm9yIGogaW4gcmFuZ2UoMSxsZW4oc3QpKToKICAgaWYgc3Rbal09PXN0W2otMV06Y3UrPTEKICAgZWxzZTpteD1tYXgobXgsY3UpO2N1PTEKICBwcmludChtYXgobXgrMSxjdSsxKSk=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
