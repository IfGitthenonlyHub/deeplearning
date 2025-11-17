import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBAbHJ1X2NhY2hlKE5vbmUpCiAgICBkZWYgd2lubmVyU3F1YXJlR2FtZShzZWxmLCBuOiBpbnQpIC0+IGJvb2w6CiAgICAgICAgcmV0dXJuIFRydWUgaWYgbiA9PSAxIGVsc2UgYW55KG5vdCBzZWxmLndpbm5lclNxdWFyZUdhbWUobiAtIGkgKiogMikgZm9yIGkgaW4gcmFuZ2UoaW50KG4gKiogMC41KSwgMCwgLTEpKQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
