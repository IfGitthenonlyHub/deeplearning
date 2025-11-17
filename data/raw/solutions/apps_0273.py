import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgcmFjZWNhcihzZWxmLCB0YXJnZXQ6IGludCkgLT4gaW50OgogICAgICAgIGRwID0gWzAsIDEsIDRdICsgW2Zsb2F0KCdpbmYnKV0gKiB0YXJnZXQKICAgICAgICBmb3IgaSBpbiByYW5nZSgzLCB0YXJnZXQrMSk6CiAgICAgICAgICAgIGsgPSBpLmJpdF9sZW5ndGgoKQogICAgICAgICAgICBpZiBpID09IDIqKmstMToKICAgICAgICAgICAgICAgIGRwW2ldID0gawogICAgICAgICAgICAgICAgY29udGludWUKICAgICAgICAgICAgCiAgICAgICAgICAgIGZvciBqIGluIHJhbmdlKGstMSk6CiAgICAgICAgICAgICAgICBkcFtpXSA9IG1pbihkcFtpXSwgZHBbaS0yKiooay0xKSArIDIqKmpdICsgay0xK2orMikKICAgICAgICAgICAgaWYgMioqay0xLWkgPCBpOgogICAgICAgICAgICAgICAgZHBbaV0gPSBtaW4oZHBbaV0sIGRwWzIqKmstMS1pXStrKzEpCiAgICAgICAgcmV0dXJuIGRwW3RhcmdldF0=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
