import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbWF4U3VtQWZ0ZXJQYXJ0aXRpb25pbmcoc2VsZiwgQTogTGlzdFtpbnRdLCBLOiBpbnQpIC0+IGludDoKICAgICAgICBkcCA9IFswIGZvciBpIGluIHJhbmdlKGxlbihBKSsxKV0KICAgICAgICBmb3IgaSBpbiByYW5nZSgxLCBsZW4oQSkrMSk6CiAgICAgICAgICAgIGRwW2ldID0gbWF4KFtkcFtpLWpdICsgaiAqIG1heChBW2ktajppXSkgZm9yIGogaW4gcmFuZ2UoMSwgSysxKSBpZiBqIDw9IGldKQogICAgICAgIHJldHVybiBkcFstMV0=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
