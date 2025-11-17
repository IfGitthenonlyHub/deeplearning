import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgZGVmIGlzU2NyYW1ibGUoc2VsZiwgczEsIHMyKToKICAgICAgICAgaWYgc29ydGVkKHMxKSAhPSBzb3J0ZWQoczIpOiByZXR1cm4gRmFsc2UKICAgICAgICAgaWYgbGVuKHMxKSA8IDQgb3IgczEgPT0gczI6IHJldHVybiBUcnVlCiAgICAgICAgIGYgPSBzZWxmLmlzU2NyYW1ibGUKICAgICAgICAgZm9yIGkgaW4gcmFuZ2UoMSwgbGVuKHMxKSk6CiAgICAgICAgICAgICBpZiBmKHMxWzppXSwgczJbOmldKSBhbmQgZihzMVtpOl0sIHMyW2k6XSkgb3IgZihzMVs6aV0sIHMyWy1pOl0pIGFuZCBmKHMxW2k6XSwgczJbOmxlbihzMSkgLSBpXSk6CiAgICAgICAgICAgICAgICAgcmV0dXJuIFRydWUKICAgICAgICAgcmV0dXJuIEZhbHNl").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
