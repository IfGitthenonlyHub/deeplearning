import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgZGVmIGZpcnN0TWlzc2luZ1Bvc2l0aXZlKHNlbGYsIG51bXMpOgogICAgICAgICBmb3IgaSBpbiByYW5nZShsZW4obnVtcykpOgogICAgICAgICAgICAgd2hpbGUgMCA8PSBudW1zW2ldLTEgPCBsZW4obnVtcykgYW5kIG51bXNbbnVtc1tpXS0xXSAhPSBudW1zW2ldOgogICAgICAgICAgICAgICAgIHRtcCA9IG51bXNbaV0tMQogICAgICAgICAgICAgICAgIG51bXNbaV0sIG51bXNbdG1wXSA9IG51bXNbdG1wXSwgbnVtc1tpXQogICAgICAgICBmb3IgaSBpbiByYW5nZShsZW4obnVtcykpOgogICAgICAgICAgICAgaWYgbnVtc1tpXSAhPSBpKzE6CiAgICAgICAgICAgICAgICAgcmV0dXJuIGkrMQogICAgICAgICByZXR1cm4gbGVuKG51bXMpKzE=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
