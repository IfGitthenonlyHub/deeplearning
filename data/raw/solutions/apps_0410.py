import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgZ2V0S3RoKHNlbGYsIGxvOiBpbnQsIGhpOiBpbnQsIGs6IGludCkgLT4gaW50OgogICAgICAgIGRlZiBnZXRQb3dlcihuKToKICAgICAgICAgICAgcmV0dXJuIDAgaWYgbiA9PSAxIGVsc2UgKGdldFBvd2VyKDMgKiBuICsgMSkgaWYgbiAlIDIgZWxzZSBnZXRQb3dlcihuIC8gMikpICsgMQogICAgICAgIHJldHVybiBzb3J0ZWQocmFuZ2UobG8sIGhpICsgMSksIGtleT1nZXRQb3dlcilbayAtIDFd").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
