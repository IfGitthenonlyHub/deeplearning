import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbnRoVWdseU51bWJlcihzZWxmLCBuOiBpbnQsIGE6IGludCwgYjogaW50LCBjOiBpbnQpIC0+IGludDoKICAgICAgICBhYiA9IGEqYi8vZ2NkKGEsIGIpCiAgICAgICAgYmMgPSBiKmMvL2djZChiLCBjKQogICAgICAgIGNhID0gYyphLy9nY2QoYywgYSkKICAgICAgICBhYmMgPSBhYipjLy9nY2QoYWIsIGMpCiAgICAgICAgCiAgICAgICAgZGVmIGZuKGspOgogICAgICAgICAgICByZXR1cm4gay8vYSArIGsvL2IgKyBrLy9jIC0gay8vYWIgLSBrLy9iYyAtIGsvL2NhICsgay8vYWJjCgogICAgICAgIGxvLCBoaSA9IDAsIDJfMDAwXzAwMF8wMDAKICAgICAgICB3aGlsZSBsbyA8IGhpOgogICAgICAgICAgICBtaWQgPSAobG8gKyBoaSkvLzIKICAgICAgICAgICAgaWYgZm4obWlkKSA+PSBuOiBoaSA9IG1pZAogICAgICAgICAgICBlbHNlOiBsbyA9IG1pZCArIDEKICAgICAgICByZXR1cm4gbG8=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
