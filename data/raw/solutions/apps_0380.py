import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgZGVmIHZhbGlkSVBBZGRyZXNzKHNlbGYsIElQKToKICAgICAgICAgCiAgICAgICAgIGRlZiBpc0lQdjQocyk6CiAgICAgICAgICAgICB0cnk6IHJldHVybiBzdHIoaW50KHMpKSA9PSBzIGFuZCAwIDw9IGludChzKSA8PSAyNTUKICAgICAgICAgICAgIGV4Y2VwdDogcmV0dXJuIEZhbHNlCiAgICAgICAgICAgICAKICAgICAgICAgZGVmIGlzSVB2NihzKToKICAgICAgICAgICAgIGlmIGxlbihzKSA+IDQ6IHJldHVybiBGYWxzZQogICAgICAgICAgICAgdHJ5OiByZXR1cm4gaW50KHMsIDE2KSA+PSAwIGFuZCBzWzBdICE9ICctJwogICAgICAgICAgICAgZXhjZXB0OiByZXR1cm4gRmFsc2UKIAogICAgICAgICBpZiBJUC5jb3VudCgiLiIpID09IDMgYW5kIGFsbChpc0lQdjQoaSkgZm9yIGkgaW4gSVAuc3BsaXQoIi4iKSk6IAogICAgICAgICAgICAgcmV0dXJuICJJUHY0IgogICAgICAgICBpZiBJUC5jb3VudCgiOiIpID09IDcgYW5kIGFsbChpc0lQdjYoaSkgZm9yIGkgaW4gSVAuc3BsaXQoIjoiKSk6IAogICAgICAgICAgICAgcmV0dXJuICJJUHY2IgogICAgICAgICByZXR1cm4gIk5laXRoZXIi").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
