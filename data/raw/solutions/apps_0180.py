import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbWluUmVmdWVsU3RvcHMoc2VsZiwgdGFyZ2V0OiBpbnQsIHN0YXJ0RnVlbDogaW50LCBzdGF0aW9uczogTGlzdFtMaXN0W2ludF1dKSAtPiBpbnQ6CiAgICAgICAgcHEgPSBbXQogICAgICAgIGlkeCA9IDAgCiAgICAgICAgY3VyID0gc3RhcnRGdWVsCiAgICAgICAgcmVzID0gMAogICAgICAgIHdoaWxlIGN1ciA8IHRhcmdldDogCiAgICAgICAgICAgIHdoaWxlIGlkeCA8IGxlbihzdGF0aW9ucykgYW5kIGN1ciA+PSBzdGF0aW9uc1tpZHhdWzBdOgogICAgICAgICAgICAgICAgaGVhcHEuaGVhcHB1c2gocHEsIC1zdGF0aW9uc1tpZHhdWzFdKQogICAgICAgICAgICAgICAgaWR4ICs9IDEKICAgICAgICAgICAgaWYgbm90IHBxOiByZXR1cm4gLTEgCiAgICAgICAgICAgIGN1ciAtPSBoZWFwcS5oZWFwcG9wKHBxKQogICAgICAgICAgICByZXMgKz0gMQogICAgICAgIHJldHVybiByZXM=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
