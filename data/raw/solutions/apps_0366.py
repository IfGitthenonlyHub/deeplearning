import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgZGVmIGxvbmdlc3RTdWJzdHJpbmcoc2VsZiwgcywgayk6CiAgICAgICAgICIiIgogICAgICAgICA6dHlwZSBzOiBzdHIKICAgICAgICAgOnR5cGUgazogaW50CiAgICAgICAgIDpydHlwZTogaW50CiAgICAgICAgICIiIgogICAgICAgICBmb3IgaSBpbiBzZXQocyk6CiAgICAgICAgICAgICBpZiBzLmNvdW50KGkpPGs6CiAgICAgICAgICAgICAgICAgcmV0dXJuIG1heChzZWxmLmxvbmdlc3RTdWJzdHJpbmcodCxrKSBmb3IgdCBpbiBzLnNwbGl0KGkpKQogICAgICAgICByZXR1cm4gbGVuKHMp").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
