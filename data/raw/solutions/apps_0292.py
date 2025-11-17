import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbWF4QWJzVmFsRXhwcihzZWxmLCBhcnIxLCBhcnIyKSAtPiBpbnQ6CiAgICAgICAgcmVzID0gMAogICAgICAgIGxlbmd0aCA9IGxlbihhcnIxKQogICAgICAgIGZvciBwLCBxIGluIFsoMSwxKSwoLTEsLTEpLCgxLC0xKSwoLTEsMSldOgogICAgICAgICAgICBtaW5fdiA9IHAqYXJyMVswXSArIHEqYXJyMlswXSArIDAKICAgICAgICAgICAgZm9yIGkgaW4gcmFuZ2UoMSwgbGVuZ3RoKToKICAgICAgICAgICAgICAgIHYgPSBwKmFycjFbaV0gKyBxKmFycjJbaV0gKyBpCiAgICAgICAgICAgICAgICByZXMgPSBtYXgocmVzLCB2IC0gbWluX3YpCiAgICAgICAgICAgICAgICBtaW5fdiA9IG1pbih2LCBtaW5fdikKICAgICAgICByZXR1cm4gcmVz").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
