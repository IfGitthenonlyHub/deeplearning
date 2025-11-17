import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgZGVmIGNhbkNyb3NzKHNlbGYsIHN0b25lcyk6CiAgICAgICAgICIiIgogICAgICAgICA6dHlwZSBzdG9uZXM6IExpc3RbaW50XQogICAgICAgICA6cnR5cGU6IGJvb2wKICAgICAgICAgIiIiCiAgICAgICAgIHRhcmdldCwgc3RvbmVzLCBtZW1vID0gc3RvbmVzWy0xXSwgc2V0KHN0b25lcyksIHNldCgpCiAgICAgICAgIAogICAgICAgICByZXR1cm4gc2VsZi5kZnMoc3RvbmVzLCAxLCAxLCB0YXJnZXQsIG1lbW8pCiAgICAgCiAgICAgZGVmIGRmcyhzZWxmLCBzdG9uZXMsIHBvcywganVtcCwgdGFyZ2V0LCBtZW1vKToKICAgICAgICAgaWYgKHBvcywganVtcCkgaW4gbWVtbzoKICAgICAgICAgICAgIHJldHVybiBGYWxzZQogICAgICAgICBpZiBwb3MgPT0gdGFyZ2V0OgogICAgICAgICAgICAgcmV0dXJuIFRydWUKICAgICAgICAgaWYgcG9zIG5vdCBpbiBzdG9uZXMgb3IganVtcCA8PSAwOgogICAgICAgICAgICAgcmV0dXJuIEZhbHNlCiAgICAgICAgIAogICAgICAgICBmb3IgaiBpbiAoanVtcC0xLCBqdW1wLCBqdW1wKzEpOgogICAgICAgICAgICAgaWYgc2VsZi5kZnMoc3RvbmVzLCBwb3MraiwgaiwgdGFyZ2V0LCBtZW1vKToKICAgICAgICAgICAgICAgICByZXR1cm4gVHJ1ZQogICAgICAgICBtZW1vLmFkZCgocG9zLCBqdW1wKSkgICAjIHJlY29yZCBiYWQgcG9zaXRpb24gYW5kIGp1bXAKICAgICAgICAgcmV0dXJuIEZhbHNl").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
