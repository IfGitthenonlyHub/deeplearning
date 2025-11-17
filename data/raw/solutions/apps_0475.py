import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgcmFuZ2VTdW0oc2VsZiwgbnVtczogTGlzdFtpbnRdLCBuOiBpbnQsIGxlZnQ6IGludCwgcmlnaHQ6IGludCkgLT4gaW50OgogICAgICAgIGxpc3R4PVtzdW0obnVtc1tpOmpdKSBmb3IgaSBpbiByYW5nZSgwLGxlbihudW1zKSkgZm9yIGogaW4gcmFuZ2UoaSsxLGxlbihudW1zKSsxKV0KICAgICAgICBsaXN0eC5zb3J0KCkKICAgICAgICByZXR1cm4gc3VtKGxpc3R4W2xlZnQtMTpyaWdodF0pJSgoMTAqKjkgKyA3KSk=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
