import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgZGVmIGZsaXBMaWdodHMoc2VsZiwgbiwgbSk6CiAgICAgICAgICIiIgogICAgICAgICA6dHlwZSBuOiBpbnQKICAgICAgICAgOnR5cGUgbTogaW50CiAgICAgICAgIDpydHlwZTogaW50CiAgICAgICAgICIiIgogICAgICAgICBpZiBuID09IDA6CiAgICAgICAgICAgICByZXR1cm4gMAogICAgICAgICBpZiBtID09IDA6CiAgICAgICAgICAgICByZXR1cm4gMQogICAgICAgICBpZiBuID09IDE6CiAgICAgICAgICAgICByZXR1cm4gMgogICAgICAgICBpZiBuID09IDIgYW5kIG0gPT0xOgogICAgICAgICAgICAgcmV0dXJuIDMKICAgICAgICAgaWYgbiA9PSAyOgogICAgICAgICAgICAgcmV0dXJuIDQKICAgICAgICAgaWYgbSA9PSAxOgogICAgICAgICAgICAgcmV0dXJuIDQKICAgICAgICAgaWYgbSA9PSAyOgogICAgICAgICAgICAgcmV0dXJuIDcKICAgICAgICAgcmV0dXJuIDg=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
