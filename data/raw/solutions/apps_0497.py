import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("aW1wb3J0IGJpc2VjdApjbGFzcyBTb2x1dGlvbjoKICAgIGRlZiBqb2JTY2hlZHVsaW5nKHNlbGYsIHN0YXJ0VGltZTogTGlzdFtpbnRdLCBlbmRUaW1lOiBMaXN0W2ludF0sIHByb2ZpdDogTGlzdFtpbnRdKSAtPiBpbnQ6CiAgICAgICAgZHA9W1swLDBdXQogICAgICAgIGN1cmluZm89c29ydGVkKGxpc3QoemlwKHN0YXJ0VGltZSxlbmRUaW1lLHByb2ZpdCkpLGtleT1sYW1iZGEgeDp4WzFdKQogICAgICAgIGZvciBzLGUscCBpbiBjdXJpbmZvOgogICAgICAgICAgICBpPWJpc2VjdC5iaXNlY3RfcmlnaHQoZHAsW3MrMV0pLTEKICAgICAgICAgICAgaWYgZHBbaV1bMV0rcD5kcFstMV1bMV06CiAgICAgICAgIAogICAgICAgICAgICAgICAgZHAuYXBwZW5kKFtlLGRwW2ldWzFdK3BdKQoKICAgICAgICByZXR1cm4gZHBbLTFdWzFd").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
