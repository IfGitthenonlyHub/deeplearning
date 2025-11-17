import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbWF4VHVyYnVsZW5jZVNpemUoc2VsZiwgQTogTGlzdFtpbnRdKSAtPiBpbnQ6CiAgICAgICAgbj1sZW4oQSkKICAgICAgICBmMD1bMF0qbgogICAgICAgIGYxPVswXSpuCiAgICAgICAgZm9yIGsgaW4gcmFuZ2Uobik6CiAgICAgICAgICAgIGYwW2tdPW1heCgxLGYxW2stMV0rMSBpZiBrPj0xIGFuZCBBW2tdPEFbay0xXSBlbHNlIDApCiAgICAgICAgICAgIGYxW2tdPW1heCgxLGYwW2stMV0rMSBpZiBrPj0xIGFuZCBBW2tdPkFbay0xXSBlbHNlIDApCiAgICAgICAgcmV0dXJuIG1heChtYXgoZjApLG1heChmMSkp").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
