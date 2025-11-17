import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbnVtT2ZNaW51dGVzKHNlbGYsIG4sIGhlYWRJRCwgbWFuYWdlciwgaW5mb3JtVGltZSk6CiAgICAgICAgZGVmIGRmcyhpKToKICAgICAgICAgICAgaWYgbWFuYWdlcltpXSAhPSAtMToKICAgICAgICAgICAgICAgIGluZm9ybVRpbWVbaV0gKz0gZGZzKG1hbmFnZXJbaV0pCiAgICAgICAgICAgICAgICBtYW5hZ2VyW2ldID0gLTEKICAgICAgICAgICAgcmV0dXJuIGluZm9ybVRpbWVbaV0KICAgICAgICByZXR1cm4gbWF4KG1hcChkZnMsIHJhbmdlKG4pKSk=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
