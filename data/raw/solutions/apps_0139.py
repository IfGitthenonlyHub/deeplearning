import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbWluRGVsZXRpb25TaXplKHNlbGYsIEEpOgogICAgICAgIG0sIG4gPSBsZW4oQSksIGxlbihBWzBdKQogICAgICAgIGZpcnN0ID0gW0ZhbHNlXSAqIG0KICAgICAgICByZXMgPSAwCiAgICAgICAgZm9yIGogaW4gcmFuZ2Uobik6CiAgICAgICAgICAgIGZvciBpIGluIHJhbmdlKDEsIG0pOgogICAgICAgICAgICAgICAgaWYgbm90IGZpcnN0W2ldIGFuZCBBW2ldW2pdIDwgQVtpIC0gMV1bal06CiAgICAgICAgICAgICAgICAgICAgcmVzICs9IDEKICAgICAgICAgICAgICAgICAgICBicmVhawogICAgICAgICAgICBlbHNlOgogICAgICAgICAgICAgICAgZm9yIGkgaW4gcmFuZ2UoMSwgbSk6CiAgICAgICAgICAgICAgICAgICAgaWYgQVtpXVtqXSA+IEFbaSAtIDFdW2pdOgogICAgICAgICAgICAgICAgICAgICAgICBmaXJzdFtpXSA9IFRydWUKICAgICAgICByZXR1cm4gcmVz").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
