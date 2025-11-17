import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbWF4RGlzdGFuY2Uoc2VsZiwgcG9zaXRpb246IExpc3RbaW50XSwgbTogaW50KSAtPiBpbnQ6CiAgICAgICAgcG9zaXRpb24uc29ydCgpCiAgICAgICAgbG8saGk9MSxwb3NpdGlvblstMV0tcG9zaXRpb25bMF0KICAgICAgICB3aGlsZSBsbzxoaToKICAgICAgICAgICAgbWksdCx5PShsbytoaSsxKS8vMiwxLHBvc2l0aW9uWzBdCiAgICAgICAgICAgIGZvciB4IGluIHBvc2l0aW9uOgogICAgICAgICAgICAgICAgaWYgeC15Pj1taTogeSx0PXgsdCsxCiAgICAgICAgICAgIGlmIHQ8bTogaGk9bWktMQogICAgICAgICAgICBlbHNlOiBsbz1taQogICAgICAgIHJldHVybiBsbw==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
