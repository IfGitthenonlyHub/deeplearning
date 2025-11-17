import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgZGVmIGNhbkNvbXBsZXRlQ2lyY3VpdChzZWxmLCBnYXMsIGNvc3QpOgogICAgICAgICAiIiIKICAgICAgICAgOnR5cGUgZ2FzOiBMaXN0W2ludF0KICAgICAgICAgOnR5cGUgY29zdDogTGlzdFtpbnRdCiAgICAgICAgIDpydHlwZTogaW50CiAgICAgICAgICIiIgogICAgICAgICBpZiBzdW0oZ2FzKSA8IHN1bShjb3N0KToKICAgICAgICAgICAgIHJldHVybiAtMQogICAgICAgICBSZXN0ID0gMAogICAgICAgICBpbmRleCA9IDAKICAgICAgICAgZm9yIGkgaW4gcmFuZ2UobGVuKGdhcykpOgogICAgICAgICAgICAgUmVzdCArPSBnYXNbaV0gLSBjb3N0W2ldCiAgICAgICAgICAgICBpZiBSZXN0IDwgMDoKICAgICAgICAgICAgICAgICBpbmRleCA9IGkgKyAxCiAgICAgICAgICAgICAgICAgUmVzdCA9IDAKICAgICAgICAgcmV0dXJuIGluZGV4").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
