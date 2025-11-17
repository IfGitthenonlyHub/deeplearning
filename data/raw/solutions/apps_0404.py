import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbGFyZ2VzdFN1bU9mQXZlcmFnZXMoc2VsZiwgQTogTGlzdFtpbnRdLCBLOiBpbnQpIC0+IGZsb2F0OgogICAgICAgIG4gPSBsZW4oQSkKICAgICAgICBkcCA9IFtbMF0qKEsrMSkgZm9yIF8gaW4gcmFuZ2UobisxKV0KICAgICAgICAKICAgICAgICBmb3IgaSBpbiByYW5nZSgxLCBuKzEpOgogICAgICAgICAgICBkcFtpXVsxXSA9IHN1bShBWzppXSkvaQogICAgICAgIGZvciBpIGluIHJhbmdlKDIsIG4rMSk6CiAgICAgICAgICAgIGZvciBqIGluIHJhbmdlKDIsIG1pbihLKzEsIGkrMSkpOgogICAgICAgICAgICAgICAgZHBbaV1bal0gPSBtYXgoW2RwW2ktdF1bai0xXSArIHN1bShBW2ktdDppXSkgLyB0IGZvciB0IGluIHJhbmdlKDEsaSldKQogICAgICAgIHJldHVybiBkcFtuXVtLXQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
