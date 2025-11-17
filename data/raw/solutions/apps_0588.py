import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("ZnJvbSBtYXRoIGltcG9ydCBnY2QKZm9yIF8gaW4gcmFuZ2UoaW50KGlucHV0KCkpKToKIG49aW50KGlucHV0KCkpCiBsPVtpbnQoeSkgZm9yIHkgaW4gaW5wdXQoKS5zcGxpdCgnICcpXQogZz1sWzFdLWxbMF0KIGNvdW50PTAKIGZvciBpIGluIHJhbmdlKDEsbik6CiAgZz1nY2QoZyxsW2ldLWxbaS0xXSkKIGc9Z2NkKGcsMzYwLWxbbi0xXStsWzBdKQogZm9yIGkgaW4gcmFuZ2UoMSwgbik6CiAgY291bnQrPShsW2ldLWxbaS0xXSkvL2ctMQogY291bnQrPSgzNjAtbFtuLTFdK2xbMF0pLy9nLTEKIHByaW50KGNvdW50KQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
