import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgb2RkRXZlbkp1bXBzKHNlbGYsIEE6IExpc3RbaW50XSkgLT4gaW50OgogICAgICAgIGRlZiBoZWxwZXIoQSk6CiAgICAgICAgICAgIGFucz1bMF0qbGVuKEEpCiAgICAgICAgICAgIHN0YWNrPVtdCiAgICAgICAgICAgIGZvciBhLGkgaW4gQToKICAgICAgICAgICAgICAgIHdoaWxlIHN0YWNrIGFuZCBzdGFja1stMV08aToKICAgICAgICAgICAgICAgICAgICBhbnNbc3RhY2sucG9wKCldPWkKICAgICAgICAgICAgICAgIHN0YWNrLmFwcGVuZChpKQogICAgICAgICAgICByZXR1cm4gYW5zCiAgICAgICAgCiAgICAgICAgb2RkPWhlbHBlcihzb3J0ZWQoW2EsaV0gZm9yIGksYSBpbiBlbnVtZXJhdGUoQSkpKQogICAgICAgIGV2ZW49aGVscGVyKHNvcnRlZChbLWEsaV0gZm9yIGksYSBpbiBlbnVtZXJhdGUoQSkpKQogICAgICAgIGw9bGVuKEEpCiAgICAgICAgb2RkanVtcCxldmVuanVtcD1bMF0qbCxbMF0qbAogICAgICAgIG9kZGp1bXBbLTFdPWV2ZW5qdW1wWy0xXT0xCiAgICAgICAgZm9yIGkgaW4gcmFuZ2UobC0xKVs6Oi0xXToKICAgICAgICAgICAgb2RkanVtcFtpXT1ldmVuanVtcFtvZGRbaV1dCiAgICAgICAgICAgIGV2ZW5qdW1wW2ldPW9kZGp1bXBbZXZlbltpXV0KICAgICAgICByZXR1cm4gc3VtKG9kZGp1bXAp").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
