import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAjIGh0dHBzOi8vbGVldGNvZGUuY29tL3Byb2JsZW1zL2xvbmdlc3QtaGFwcHktc3RyaW5nL2Rpc2N1c3MvNTY0Mjc3L0MlMkIlMkJKYXZhLWEtZ3JlYXRlci1iLWdyZWF0ZXItYwogICAgZGVmIGxvbmdlc3REaXZlcnNlU3RyaW5nKHNlbGYsIGE6IGludCwgYjogaW50LCBjOiBpbnQsIGNoYXJBID0gJ2EnLCBjaGFyQiA9ICdiJywgY2hhckMgPSAnYycpIC0+IHN0cjoKICAgICAgICBpZiBhPGI6IAogICAgICAgICAgICByZXR1cm4gc2VsZi5sb25nZXN0RGl2ZXJzZVN0cmluZyhiLCBhLCBjLCBjaGFyQiwgY2hhckEsIGNoYXJDKQogICAgICAgIGlmIGI8YzogCiAgICAgICAgICAgIHJldHVybiBzZWxmLmxvbmdlc3REaXZlcnNlU3RyaW5nKGEsIGMsIGIsIGNoYXJBLCBjaGFyQywgY2hhckIpCiAgICAgICAgIyBwcmludChhLCBiLCBjLCBjaGFyQSwgY2hhckIsIGNoYXJDKQogICAgICAgIGlmIGI9PTA6IAogICAgICAgICAgICByZXR1cm4gbWluKGEsIDIpKmNoYXJBIAogICAgICAgIHVzZV9hID0gbWluKDIsIGEpCiAgICAgICAgdXNlX2IgPSAxIGlmIGEtdXNlX2E+PWIgZWxzZSAwIAogICAgICAgIHJldHVybiBjaGFyQSp1c2VfYSArIGNoYXJCKnVzZV9iICsgc2VsZi5sb25nZXN0RGl2ZXJzZVN0cmluZyhhLXVzZV9hLCBiLXVzZV9iLCBjLCBjaGFyQSwgY2hhckIsIGNoYXJDKQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
