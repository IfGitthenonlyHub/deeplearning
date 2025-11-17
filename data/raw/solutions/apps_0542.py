import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Zm9yIF8gaW4gcmFuZ2UoaW50KGlucHV0KCkpKToKICAgIE4sTSA9IFtpbnQoeCkgZm9yIHggaW4gaW5wdXQoKS5zcGxpdCgpXQogICAgTGlzdCA9IFtdCiAgICBmb3IgaSBpbiByYW5nZShOKToKICAgICAgICBUZW1wID0gW3ggZm9yIHggaW4gaW5wdXQoKV0KICAgICAgICBMaXN0LmFwcGVuZChUZW1wKQogICAgQW5zID0gMAogICAgZm9yIGkgaW4gcmFuZ2UoTik6CiAgICAgICAgZm9yIGogaW4gcmFuZ2UoTSk6CiAgICAgICAgICAgIHg9MQogICAgICAgICAgICB3aGlsZShpK3g8TiBhbmQgait4PE0pOgogICAgICAgICAgICAgICAgaWYoTGlzdFtpXVtqXT09TGlzdFtpXVtqK3hdPT1MaXN0W2kreF1bal09PUxpc3RbaSt4XVtqK3hdKToKICAgICAgICAgICAgICAgICAgICBBbnMrPTEKICAgICAgICAgICAgICAgIHgrPTEKICAgIHByaW50KEFucyk=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
