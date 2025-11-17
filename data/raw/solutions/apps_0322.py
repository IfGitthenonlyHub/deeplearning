import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgZGVmIG1pblBhdGNoZXMoc2VsZiwgbnVtcywgbik6CiAgICAgICAgICIiIgogICAgICAgICA6dHlwZSBudW1zOiBMaXN0W2ludF0KICAgICAgICAgOnR5cGUgbjogaW50CiAgICAgICAgIDpydHlwZTogaW50CiAgICAgICAgICIiIgogICAgICAgICByZXMsIGN1ciwgaSA9IDAsIDEsIDAKICAgICAgICAgd2hpbGUgY3VyIDw9IG46CiAgICAgICAgICAgICBpZiBpIDwgbGVuKG51bXMpIGFuZCBudW1zW2ldIDw9IGN1cjoKICAgICAgICAgICAgICAgICBjdXIgKz0gbnVtc1tpXQogICAgICAgICAgICAgICAgIGkgKz0gMQogICAgICAgICAgICAgZWxzZToKICAgICAgICAgICAgICAgICBjdXIgKj0gMgogICAgICAgICAgICAgICAgIHJlcyArPSAxCiAgICAgICAgIHJldHVybiByZXM=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
