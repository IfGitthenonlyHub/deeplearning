import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("ZCA9IFswXSAqIDQ5MDExCgpkZWYgZyhuLCBtLCBrKToKICAgIHQgPSAxZTkKICAgIGZvciBpIGluIHJhbmdlKDEsIG0gLy8gMiArIDEpOgogICAgICAgIGZvciBqIGluIHJhbmdlKGsgKyAxKToKICAgICAgICAgICAgdCA9IG1pbih0LCBmKG4sIG0gLSBpLCBrIC0gaikgKyBmKG4sIGksIGopKQogICAgcmV0dXJuIG4gKiBuICsgdAoKZGVmIGYobiwgbSwgayk6CiAgICBpZiBuID4gbTogbiwgbSA9IG0sIG4KICAgIGsgPSBtaW4oaywgbiAqIG0gLSBrKQogICAgaWYgayA9PSAwOiByZXR1cm4gMAogICAgaWYgayA8IDA6IHJldHVybiAxZTkKICAgIHEgPSBuICsgMzEgKiBtICsgOTYxICogawogICAgaWYgZFtxXSA9PSAwOiBkW3FdID0gbWluKGcobiwgbSwgayksIGcobSwgbiwgaykpCiAgICByZXR1cm4gZFtxXQoKZm9yIHEgaW4gcmFuZ2UoaW50KGlucHV0KCkpKToKICAgIG4sIG0sIGsgPSBtYXAoaW50LCBpbnB1dCgpLnNwbGl0KCkpCiAgICBwcmludChmKG4sIG0sIGspKQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
