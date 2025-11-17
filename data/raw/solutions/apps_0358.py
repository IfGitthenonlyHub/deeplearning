import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgZmluZFJlcGxhY2VTdHJpbmcoc2VsZiwgUzogc3RyLCBpbmRleGVzOiBMaXN0W2ludF0sIHNvdXJjZXM6IExpc3Rbc3RyXSwgdGFyZ2V0czogTGlzdFtzdHJdKSAtPiBzdHI6CiAgICAgICAgZm9yIGksIHMsIHQgaW4gc29ydGVkKHppcChpbmRleGVzLCBzb3VyY2VzLCB0YXJnZXRzKSwgcmV2ZXJzZT1UcnVlKToKICAgICAgICAgICAgaWYgU1tpOmkgKyBsZW4ocyldID09IHM6CiAgICAgICAgICAgICAgICBTID0gU1s6aV0gKyB0ICsgU1tpICsgbGVuKHMpOl0KICAgICAgICByZXR1cm4gUw==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
