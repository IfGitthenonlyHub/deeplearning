import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbWF4RG90UHJvZHVjdChzZWxmLCBudW1zMTogTGlzdFtpbnRdLCBudW1zMjogTGlzdFtpbnRdKSAtPiBpbnQ6CiAgICAgICAgQGxydV9jYWNoZShOb25lKQogICAgICAgIGRlZiBkcChpLGopOgogICAgICAgICAgICBpZiBpPDAgb3IgajwwOgogICAgICAgICAgICAgICAgcmV0dXJuIC1mbG9hdCgnaW5mJykKICAgICAgICAgICAgcmV0dXJuIG1heChudW1zMVtpXSpudW1zMltqXSwgbnVtczFbaV0qbnVtczJbal0rZHAoaS0xLGotMSksIGRwKGksIGotMSksIGRwKGktMSwgaikpCiAgICAgICAgcmV0dXJuIGRwKGxlbihudW1zMSktMSwgbGVuKG51bXMyKS0xKQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
