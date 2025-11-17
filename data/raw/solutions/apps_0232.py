import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgZGVmIGZpbmRQb2lzb25lZER1cmF0aW9uKHNlbGYsIHRpbWVTZXJpZXMsIGR1cmF0aW9uKToKICAgICAgICAgIiIiCiAgICAgICAgIDp0eXBlIHRpbWVTZXJpZXM6IExpc3RbaW50XQogICAgICAgICA6dHlwZSBkdXJhdGlvbjogaW50CiAgICAgICAgIDpydHlwZTogaW50CiAgICAgICAgICIiIgogICAgICAgICByZXR1cm4gc3VtKG1pbihkdXJhdGlvbiwgYiAtIGEpIGZvciBhLCBiIGluIHppcCh0aW1lU2VyaWVzLCB0aW1lU2VyaWVzWzE6XSArIFsxMGU3XSkp").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
