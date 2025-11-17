import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgZGlzdGluY3RFY2hvU3Vic3RyaW5ncyhzZWxmLCB0ZXh0OiBzdHIpIC0+IGludDoKICAgICAgICBvdXQgPSBzZXQoKQogICAgICAgIGZvciBpIGluIHJhbmdlKGxlbih0ZXh0KS0xKToKICAgICAgICAgICAgZm9yIGogaW4gcmFuZ2UoaSsxLGxlbih0ZXh0KSk6CiAgICAgICAgICAgICAgICBpZiB0ZXh0W2k6al09PXRleHRbajoyKmogLWldOgogICAgICAgICAgICAgICAgICAgIG91dC5hZGQodGV4dFtpOmpdKQogICAgICAgIHJldHVybiBsZW4ob3V0KQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
