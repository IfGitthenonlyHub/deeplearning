import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("aW1wb3J0IHN5cwoKaW5wdXQgPSBzeXMuc3RkaW4ucmVhZGxpbmUKCmZvciBfIGluIHJhbmdlKGludChpbnB1dCgpKSk6CiAgICBuLCBrID0gbGlzdChtYXAoaW50LCBpbnB1dCgpLnNwbGl0KCkpKQogICAgYSA9IGxpc3QobWFwKGludCwgaW5wdXQoKS5zcGxpdCgpKSkKICAgIHBlYWsgPSBbMF0gKyBbMSBpZiBhW2kgLSAxXSA8IGFbaV0gYW5kIGFbaV0gPiBhW2kgKyAxXSBlbHNlIDAgZm9yIGkgaW4gcmFuZ2UoMSwgbiAtIDEpXSArIFswXQogICAgYiA9IFtOb25lXSAqIChuIC0gayArIDEpCiAgICBiWzBdID0gc3VtKHBlYWtbMSA6IGsgLSAxXSkKICAgIGZvciBpIGluIHJhbmdlKDEsIG4gLSBrICsgMSk6CiAgICAgICAgYltpXSA9IGJbaSAtIDFdIC0gcGVha1tpXSArIHBlYWtbaSArIGsgLSAyXQogICAgcCA9IG1heChiKSAgICAKICAgIHByaW50KHAgKyAxLCBiLmluZGV4KHApICsgMSk=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
