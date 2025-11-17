import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgZGVmIGNhbmR5KHNlbGYsIHJhdGluZ3MpOgogICAgICAgICAiIiIKICAgICAgICAgOnR5cGUgcmF0aW5nczogTGlzdFtpbnRdCiAgICAgICAgIDpydHlwZTogaW50CiAgICAgICAgICIiIgogICAgICAgICBuID0gbGVuKHJhdGluZ3MpCiAgICAgICAgIHJlc3VsdCA9IFsxXSAqIG4KICAgICAgICAgCiAgICAgICAgIGZvciBpIGluIHJhbmdlKG4tMSk6CiAgICAgICAgICAgICBpZiByYXRpbmdzW2krMV0+IHJhdGluZ3NbaV06CiAgICAgICAgICAgICAgICAgcmVzdWx0W2krMV0gPSByZXN1bHRbaV0gKyAxCiAgICAgICAgIAogICAgICAgICBmb3IgaSBpbiByYW5nZShuLTEsMCwtMSk6CiAgICAgICAgICAgICBpZiByYXRpbmdzW2ktMV0gPiByYXRpbmdzW2ldOgogICAgICAgICAgICAgICAgIHJlc3VsdFtpLTFdID0gbWF4KHJlc3VsdFtpXSsxLCByZXN1bHRbaS0xXSkKICAgICAgICAgICAgICAgICAKICAgICAgICAgcmV0dXJuIHN1bShyZXN1bHQp").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
