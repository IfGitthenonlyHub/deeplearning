import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("IyEgL3Vzci9iaW4vZW52IHB5dGhvbgoKZnJvbSBzeXMgaW1wb3J0IHN0ZGluCmZyb20gZnVuY3Rvb2xzIGltcG9ydCByZWR1Y2UKCmRlZiBnY2QoYSxiKToKCXdoaWxlIGIhPTA6CgkJYSxiPWIsYSViCglyZXR1cm4gYQoJCmRlZiBnY2RsKGwpOgoJcmV0dXJuIHJlZHVjZShnY2QsIGxbMTpdLGxbMF0pCgpkZWYgX19zdGFydGluZ19wb2ludCgpOgoJVD1pbnQoc3RkaW4ucmVhZGxpbmUoKSkKCWZvciBjYXNlIGluIHJhbmdlKFQpOgoJCW51bWJlcnM9bGlzdChtYXAoaW50LCBzdGRpbi5yZWFkbGluZSgpLnNwbGl0KClbMTpdKSkKCQlnPWdjZGwobnVtYmVycykKCQkKCQludW1iZXJzPVtuL2cgZm9yIG4gaW4gbnVtYmVyc10KCQlwcmludCgiICIuam9pbihbc3RyKHgpIGZvciB4IGluIG51bWJlcnNdKSkKCl9fc3RhcnRpbmdfcG9pbnQoKQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
