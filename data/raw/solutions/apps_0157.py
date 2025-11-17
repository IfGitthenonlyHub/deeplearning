import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgZGVmIGlzTWF0Y2goc2VsZiwgcywgcCk6CiAgICAgICAgICIiIgogICAgICAgICA6dHlwZSBzOiBzdHIKICAgICAgICAgOnR5cGUgcDogc3RyCiAgICAgICAgIDpydHlwZTogYm9vbAogICAgICAgICAiIiIKICAgICAgICAgbSA9IGxlbihzKQogICAgICAgICBuID0gbGVuKHApCiAgICAgICAgIHN0YXJqID0gLTEKICAgICAgICAgbGFzdF9tYXRjaCA9IC0xCiAgICAgICAgIGkgPSBqID0gMAogICAgICAgICB3aGlsZSBpPG06CiAgICAgICAgICAgICBpZiBqPG4gYW5kIChzW2ldPT1wW2pdIG9yIHBbal09PSc/Jyk6CiAgICAgICAgICAgICAgICAgaSs9MQogICAgICAgICAgICAgICAgIGorPTEKICAgICAgICAgICAgIGVsaWYgajxuIGFuZCBwW2pdPT0nKic6CiAgICAgICAgICAgICAgICAgc3RhcmogPSBqCiAgICAgICAgICAgICAgICAgaiArPSAxCiAgICAgICAgICAgICAgICAgbGFzdF9tYXRjaCA9IGkKICAgICAgICAgICAgIGVsaWYgc3RhcmohPS0xOgogICAgICAgICAgICAgICAgIGogPSBzdGFyaisxCiAgICAgICAgICAgICAgICAgbGFzdF9tYXRjaCArPTEKICAgICAgICAgICAgICAgICBpID0gbGFzdF9tYXRjaAogICAgICAgICAgICAgZWxzZToKICAgICAgICAgICAgICAgICByZXR1cm4gRmFsc2UKICAgICAgICAgCiAgICAgICAgIHdoaWxlIGo8biBhbmQgcFtqXT09JyonOgogICAgICAgICAgICAgais9MQogICAgICAgICByZXR1cm4gaj09bg==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
