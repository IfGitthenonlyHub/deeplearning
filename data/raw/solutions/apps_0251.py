import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgY2x1bXN5KHNlbGYsIE46IGludCkgLT4gaW50OgogICAgICAgIHggPSBbJyonLCAnLy8nLCAnKycsICctJ10gKiAoMTAwMDAvLzQpCiAgICAgICAgeCA9IGl0ZXIoeCkKICAgICAgICBhbnMgPSBzdHIoTikKICAgICAgICBpID0gTi0xCiAgICAgICAgd2hpbGUgaSA+IDA6CiAgICAgICAgICAgIG9wID0gbmV4dCh4KQogICAgICAgICAgICBhbnMgKz0gKG9wK3N0cihpKSkKICAgICAgICAgICAgaSAtPSAxCiAgICAgICAgcmV0dXJuIGV2YWwoYW5zKQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
