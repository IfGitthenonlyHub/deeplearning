import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbnVtYmVyV2F5cyhzZWxmLCBoYXRzOiBMaXN0W0xpc3RbaW50XV0pIC0+IGludDogICAgICAgIAogICAgICAgIGhhdDJwcGwgPSBkZWZhdWx0ZGljdChzZXQpICAgICAgICAKICAgICAgICBmb3IgcCwgaGF0c19pIGluIGVudW1lcmF0ZShoYXRzKToKICAgICAgICAgICAgZm9yIGggaW4gaGF0c19pOiBoYXQycHBsW2hdLmFkZChwKQoKICAgICAgICBNLCBuID0gMTAqKjkgKyA3LCAxIDw8IGxlbihoYXRzKQogICAgICAgIGRwID0gWzBdKm4KICAgICAgICBkcFswXSA9IDEKICAgICAgICBmb3IgaCBpbiBoYXQycHBsOgogICAgICAgICAgICBmb3IgaiBpbiByYW5nZShuLTEsIC0xLCAtMSk6CiAgICAgICAgICAgICAgICBmb3IgcCBpbiBoYXQycHBsW2hdOiAgICAgICAKICAgICAgICAgICAgICAgICAgICBpZiBqICYgKDEgPDwgcCk6ICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgIGRwW2pdID0gKGRwW2pdICsgZHBbaiBeICgxIDw8IHApXSkgJSBNICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgcmV0dXJuIGRwWy0xXQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
