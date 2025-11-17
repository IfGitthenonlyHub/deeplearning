import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbWF4U2F0aXNmaWVkKHNlbGYsIGN1c3RvbWVyczogTGlzdFtpbnRdLCBncnVtcHk6IExpc3RbaW50XSwgWDogaW50KSAtPiBpbnQ6CiAgICAgICAgYmFzZSA9IHN1bShjIGZvciBjLCBnIGluIHppcChjdXN0b21lcnMsIGdydW1weSkgaWYgZyA9PSAwKQogICAgICAgIG5jdXMgPSBbYyBpZiBnID09IDEgZWxzZSAwIGZvciBjLCBnIGluIHppcChjdXN0b21lcnMsIGdydW1weSldCiAgICAgICAgbGVuZ3RoID0gbGVuKGN1c3RvbWVycykKICAgICAgICByZXR1cm4gYmFzZSArIG1heChzdW0obmN1c1tpOmkrWF0pIGZvciBpIGluIHJhbmdlKDAsIGxlbmd0aC1YKzEpKQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
