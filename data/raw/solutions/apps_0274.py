import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("ZnJvbSBzb3J0ZWRjb250YWluZXJzIGltcG9ydCBTb3J0ZWRMaXN0CmNsYXNzIFNvbHV0aW9uOgogICAgZGVmIGxvbmdlc3RTdWJhcnJheShzZWxmLCBudW1zOiBMaXN0W2ludF0sIGxpbWl0OiBpbnQpIC0+IGludDoKICAgICAgICBzID0gU29ydGVkTGlzdCgpCiAgICAgICAgaiA9IGFucyA9IDAKICAgICAgICBmb3IgaSwgdmFsIGluIGVudW1lcmF0ZShudW1zKToKICAgICAgICAgICAgcy5hZGQodmFsKQogICAgICAgICAgICB3aGlsZSBzIGFuZCBzWy0xXSAtIHNbMF0gPiBsaW1pdDoKICAgICAgICAgICAgICAgIHMucmVtb3ZlKG51bXNbal0pCiAgICAgICAgICAgICAgICBqICs9IDEKICAgICAgICAgICAgYW5zID0gbWF4KGFucywgKGkgLSBqICsgMSkpCiAgICAgICAgcmV0dXJuIGFucw==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
