import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Zm9yIGkgaW4gcmFuZ2UoaW50KGlucHV0KCkpKToKICAgIG4gPSBpbnQoaW5wdXQoKSkKICAgIGMgPSBsaXN0KG1hcChpbnQsIGlucHV0KCkuc3BsaXQoKSkpCiAgICBkID0ge30KICAgIGRbMF0gPSAtMQogICAgcGFyaXR5ID0gMAogICAgYW5zID0gMAogICAgZm9yIGkgaW4gcmFuZ2Uobik6CiAgICAgcGFyaXR5IF49IDEgPDwgKGNbaV0tMSkKICAgICBmb3IgdCBpbiByYW5nZSgzMCk6CiAgICAgIHggPSBwYXJpdHleKDE8PHQpCiAgICAgIGlmKHggaW4gZC5rZXlzKCkpOgogICAgICAgYW5zID0gbWF4KGFucywgaSAtIGRbeF0pCiAgICAgaWYgcGFyaXR5IG5vdCBpbiBkLmtleXMoKToKICAgICAgZFtwYXJpdHldID0gaQogICAgcHJpbnQoYW5zLy8yKQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
