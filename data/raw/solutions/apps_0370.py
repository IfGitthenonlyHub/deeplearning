import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgZGVmIGxhcmdlc3RDb21wb25lbnRTaXplKHNlbGYsIEEpOgogICAgcCA9IGxpc3QocmFuZ2UobWF4KEEpICsgMSkpCiAgICAgICAKICAgIGRlZiBmaW5kKHgpOgogICAgICB3aGlsZSBwW3hdICE9IHg6CiAgICAgICAgcFt4XSA9IHBbcFt4XV0KICAgICAgICB4ID0gcFt4XQogICAgICByZXR1cm4geAogICAgCiAgICBkZWYgdW5pb24oeCwgeSk6CiAgICAgIHBbZmluZCh4KV0gPSBwW2ZpbmQoeSldICAgICAgCiAgICAgIAogICAgZm9yIGEgaW4gQTogICAgIAogICAgICBmb3IgayBpbiByYW5nZSgyLCBpbnQobWF0aC5zcXJ0KGEpICsgMSkpOiAgICAKICAgICAgICBpZiBhICUgayA9PSAwOgogICAgICAgICAgdW5pb24oYSwgYSAvLyBrKQogICAgICAgICAgdW5pb24oYSwgaykKICAgIHJldHVybiBjb2xsZWN0aW9ucy5Db3VudGVyKFtmaW5kKGEpIGZvciBhIGluIEFdKS5tb3N0X2NvbW1vbigxKVswXVsxXQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
