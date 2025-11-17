import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbWluRWF0aW5nU3BlZWQoc2VsZiwgcGlsZXM6IExpc3RbaW50XSwgSDogaW50KSAtPiBpbnQ6CiAgICAgICAgbCwgciA9IDEsIG1heChwaWxlcykKICAgICAgICB3aGlsZSBsIDwgcjoKICAgICAgICAgICAgbSA9IChsICsgcikgLy8gMgogICAgICAgICAgICBpZiBzdW0oKHAgKyBtIC0gMSkgLy8gbSBmb3IgcCBpbiBwaWxlcykgPiBIOiBsID0gbSArIDEKICAgICAgICAgICAgZWxzZTogciA9IG0KICAgICAgICByZXR1cm4gbA==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
