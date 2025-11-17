import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgZGVmIGlzVmFsaWRTZXJpYWxpemF0aW9uKHNlbGYsIHByZW9yZGVyKToKICAgICAgICAgIiIiCiAgICAgICAgIDp0eXBlIHByZW9yZGVyOiBzdHIKICAgICAgICAgOnJ0eXBlOiBib29sCiAgICAgICAgICIiIgogICAgICAgICBpZiBub3QgcHJlb3JkZXI6CiAgICAgICAgICAgICByZXR1cm4gVHJ1ZQogICAgICAgICBhcnIgPSBwcmVvcmRlci5zcGxpdCgnLCcpCiAgICAgICAgIHMgPSBbXQogICAgICAgICBmb3IgYSBpbiBhcnI6CiAgICAgICAgICAgICBzLmFwcGVuZChhKQogICAgICAgICAgICAgd2hpbGUgbGVuKHMpPj0zIGFuZCBzWy0xXT09JyMnIGFuZCBzWy0yXT09JyMnIGFuZCBzWy0zXSE9JyMnOgogICAgICAgICAgICAgICAgIHMucG9wKCkKICAgICAgICAgICAgICAgICBzLnBvcCgpCiAgICAgICAgICAgICAgICAgcy5wb3AoKQogICAgICAgICAgICAgICAgIHMuYXBwZW5kKCcjJykKICAgICAgICAgaWYgcz09WycjJ106CiAgICAgICAgICAgICByZXR1cm4gVHJ1ZQogICAgICAgICByZXR1cm4gRmFsc2U=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
