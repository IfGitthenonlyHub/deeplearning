import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbG9uZ2VzdENvbW1vblN1YnNlcXVlbmNlKHNlbGYsIHRleHQxOiBzdHIsIHRleHQyOiBzdHIpIC0+IGludDoKICAgICAgICAKICAgICAgICBkcCA9IGRlZmF1bHRkaWN0KGludCkKICAgICAgICBmb3IgaSwgYzEgaW4gZW51bWVyYXRlKHRleHQxKToKICAgICAgICAgICAgZm9yIGosIGMyIGluIGVudW1lcmF0ZSh0ZXh0Mik6CiAgICAgICAgICAgICAgICBkcFtpLGpdICA9IG1heChkcFtpLTEsIGotMV0gKyAoYzE9PWMyKSwgZHBbaS0xLGpdLCBkcFtpLGotMV0pCiAgICAgICAgICAgICAgICAKICAgICAgICByZXR1cm4gZHBbbGVuKHRleHQxKS0xLCBsZW4odGV4dDIpLTFd").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
