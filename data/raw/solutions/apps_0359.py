import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbWluRmFsbGluZ1BhdGhTdW0oc2VsZiwgQTogTGlzdFtMaXN0W2ludF1dKSAtPiBpbnQ6CiAgICAgICAgZHAgPSBbQVswXVs6XSwgWzAgZm9yIF8gaW4gQVswXV1dCiAgICAgICAgZm9yIGkgaW4gcmFuZ2UoMSwgbGVuKEEpKToKICAgICAgICAgICAgZm9yIGogaW4gcmFuZ2UobGVuKEFbaV0pKToKICAgICAgICAgICAgICAgIGRwW2kgJiAxXVtqXSA9IG1pbihbZHBbKGkgLSAxKSAmIDFdW2ogKyBrXSBmb3IgayBpbiAoLTEsIDAsIDEpIGlmIDAgPD0gaiArIGsgPCBsZW4oQVtpXSldKSArIEFbaV1bal0KICAgICAgICByZXR1cm4gbWluKGRwWyhsZW4oQSkgLSAxKSAmIDFdKQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
