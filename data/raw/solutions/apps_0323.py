import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgZGVmIGlzSW50ZXJsZWF2ZShzZWxmLCBzMSwgczIsIHMzKToKICAgICAgICAgbDEsIGwyID0gbGVuKHMxKSwgbGVuKHMyKQogICAgICAgICBpZiBsZW4oczMpIT1sMStsMjogcmV0dXJuIEZhbHNlCiAgICAgICAgIGlmIGwxPT0wIG9yIGwyPT0wOiByZXR1cm4gKGwxIGFuZCBzMT09czMpIG9yIChsMiBhbmQgczI9PXMzKSBvciBub3QgczMKICAgICAgICAgZHAgPSBbW0ZhbHNlXSoobDIrMSkgZm9yIF8gaW4gcmFuZ2UobDErMSldCiAgICAgICAgIGRwWzBdWzBdID0gVHJ1ZQogICAgICAgICBmb3IgaSBpbiByYW5nZShsMSk6CiAgICAgICAgICAgICBpZiBzMVtpXT09czNbaV06IGRwW2krMV1bMF09VHJ1ZQogICAgICAgICAgICAgZWxzZTogYnJlYWsKICAgICAgICAgZm9yIGkgaW4gcmFuZ2UobDIpOgogICAgICAgICAgICAgaWYgczJbaV09PXMzW2ldOiBkcFswXVtpKzFdPVRydWUKICAgICAgICAgICAgIGVsc2U6IGJyZWFrCiAgICAgICAgIGZvciBpIGluIHJhbmdlKDEsIGwxKzEpOgogICAgICAgICAgICAgZm9yIGogaW4gcmFuZ2UoMSwgbDIrMSk6CiAgICAgICAgICAgICAgICAgZHBbaV1bal0gPSAoczFbaS0xXT09czNbaStqLTFdIGFuZCBkcFtpLTFdW2pdKSBvciAoczJbai0xXT09czNbaStqLTFdIGFuZCBkcFtpXVtqLTFdKQogICAgICAgICByZXR1cm4gZHBbLTFdWy0xXQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
