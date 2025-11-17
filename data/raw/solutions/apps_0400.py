import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgZGVmIGxhcmdlc3RSZWN0YW5nbGVBcmVhKHNlbGYsIGhlaWdodHMpOgogICAgICAgICAiIiIKICAgICAgICAgOnR5cGUgaGVpZ2h0czogTGlzdFtpbnRdCiAgICAgICAgIDpydHlwZTogaW50CiAgICAgICAgICIiIgogICAgICAgICBhbnMsIHN0YWNrID0gMCwgW10KICAgICAgICAgZm9yIGkgaW4gcmFuZ2UobGVuKGhlaWdodHMpKToKICAgICAgICAgICAgIHdoaWxlIHN0YWNrIGFuZCBoZWlnaHRzW2ldIDwgaGVpZ2h0c1tzdGFja1stMV1dOgogICAgICAgICAgICAgICAgIGggPSBoZWlnaHRzW3N0YWNrLnBvcCgpXQogICAgICAgICAgICAgICAgIHcgPSAoaSAtIDEgLSBzdGFja1stMV0pIGlmIHN0YWNrIGVsc2UgaQogICAgICAgICAgICAgICAgIGFucyA9IG1heChhbnMsIGggKiB3KQogICAgICAgICAgICAgc3RhY2suYXBwZW5kKGkpCiAgICAgICAgIAogICAgICAgICB3aGlsZSBzdGFjazoKICAgICAgICAgICAgIGggPSBoZWlnaHRzW3N0YWNrLnBvcCgpXQogICAgICAgICAgICAgdyA9IChsZW4oaGVpZ2h0cykgLSAxIC0gc3RhY2tbLTFdKSBpZiBzdGFjayBlbHNlIGxlbihoZWlnaHRzKQogICAgICAgICAgICAgYW5zID0gbWF4KGFucywgaCAqIHcpCiAgICAgICAgIHJldHVybiBhbnM=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
