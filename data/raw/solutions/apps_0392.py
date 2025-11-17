import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbnVtV2F5cyhzZWxmLCBzOiBzdHIpIC0+IGludDoKICAgICAgICBuID0gcy5jb3VudCgnMScpCiAgICAgICAgaWYgbiAlIDMgIT0gMDogcmV0dXJuIDAKICAgICAgICBpZiBuID09IDA6IHJldHVybiAoKChsZW4ocykgLSAxKSAqIChsZW4ocykgLSAyKSkgLy8gMikgJSAoMTAqKjkgKyA3KQogICAgICAgIG0gPSBuIC8vIDMKICAgICAgICBMID0gcy5zcGxpdCgnMScpCiAgICAgICAgcmV0dXJuICgobGVuKExbbV0pICsgMSkgKiAobGVuKExbMiptXSkgKyAxKSkgJSAoMTAqKjkgKyA3KQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
