import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgZGVmIGNvbnZlcnQoc2VsZiwgcywgblJvd3MpOgogICAgICAgICBpZiBuUm93cz09MTogcmV0dXJuIHMKICAgICAgICAgdG1wPVsnJyBmb3IgaSBpbiByYW5nZShuUm93cyldCiAgICAgICAgIGluZGV4PS0xOyBzdGVwPTEKICAgICAgICAgZm9yIGkgaW4gcmFuZ2UobGVuKHMpKToKICAgICAgICAgICAgIGluZGV4Kz1zdGVwCiAgICAgICAgICAgICBpZiBpbmRleD09blJvd3M6CiAgICAgICAgICAgICAgICAgaW5kZXgtPTI7IHN0ZXA9LTEKICAgICAgICAgICAgIGVsaWYgaW5kZXg9PS0xOgogICAgICAgICAgICAgICAgIGluZGV4PTE7IHN0ZXA9MQogICAgICAgICAgICAgdG1wW2luZGV4XSs9c1tpXQogICAgICAgICByZXR1cm4gJycuam9pbih0bXAp").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
