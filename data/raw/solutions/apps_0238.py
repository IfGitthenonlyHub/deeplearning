import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgZGVmIG1heFByb2ZpdChzZWxmLCBwcmljZXMsIGsgPSAyKToKICAgICAgICAgIiIiCiAgICAgICAgIDp0eXBlIHByaWNlczogTGlzdFtpbnRdCiAgICAgICAgIDpydHlwZTogaW50CiAgICAgICAgICIiIgogICAgICAgICBpZiBub3QgcHJpY2VzOgogICAgICAgICAgICAgcmV0dXJuIDAKICAgICAgICAgCiAgICAgICAgIHMxID0gczIgPSAwCiAgICAgICAgIGIxID0gYjIgPSAtMTAwMDAwMDAwMAogICAgICAgICAKICAgICAgICAgZm9yIHAgaW4gcHJpY2VzOgogICAgICAgICAgICAgYjEgPSBtYXgoYjEsIC1wKQogICAgICAgICAgICAgczEgPSBtYXgoczEsIGIxICsgcCkKICAgICAgICAgICAgIGIyID0gbWF4KGIyLCBzMSAtIHApCiAgICAgICAgICAgICBzMiA9IG1heChzMiwgYjIgKyBwKQogICAgICAgICAKICAgICAgICAgcmV0dXJuIHMy").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
