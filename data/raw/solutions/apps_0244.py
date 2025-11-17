import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbnVtU3RlcHMoc2VsZiwgczogc3RyKSAtPiBpbnQ6CiAgICAgICAgaSwgbWlkX3plcm8gPSAwICwgMCAKICAgICAgICBmb3IgaiBpbiByYW5nZSgxLCBsZW4ocykpOgogICAgICAgICAgICBpZiBzW2pdID09ICcxJzoKICAgICAgICAgICAgICAgIG1pZF96ZXJvICs9IGogLWkgLSAxCiAgICAgICAgICAgICAgICBpID0gagogICAgICAgIGlmIGkgPT0gMDoKICAgICAgICAgICAgcmV0dXJuIGxlbihzKS0xCiAgICAgICAgcmV0dXJuIG1pZF96ZXJvICsgMSArIGxlbihzKQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
