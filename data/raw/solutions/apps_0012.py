import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("dCA9IGludChpbnB1dCgpKQpmb3IgXyBpbiByYW5nZSh0KToKICAgIG4gPSBpbnQoaW5wdXQoKSkKICAgIEEgPSBtYXAoaW50LCBpbnB1dCgpLnNwbGl0KCkpCiAgICBCID0gbWFwKGludCwgaW5wdXQoKS5zcGxpdCgpKQogICAgCiAgICBzZWVuX3BvcyA9IHNlZW5fbmVnID0gRmFsc2UKICAgIGZvciBhLCBiIGluIHppcChBLCBCKToKICAgICAgICBpZiAoYiA+IGEgYW5kIG5vdCBzZWVuX3Bvcykgb3IgKGIgPCBhIGFuZCBub3Qgc2Vlbl9uZWcpOgogICAgICAgICAgICBwcmludCgnTk8nKQogICAgICAgICAgICBicmVhawogICAgICAgIAogICAgICAgIGlmIGEgPiAwOgogICAgICAgICAgICBzZWVuX3BvcyA9IFRydWUKICAgICAgICBlbGlmIGEgPCAwOgogICAgICAgICAgICBzZWVuX25lZyA9IFRydWUgICAgICAgIAogICAgZWxzZToKICAgICAgICBwcmludCgnWUVTJyk=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
