import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgaXNSb2JvdEJvdW5kZWQoc2VsZiwgaW5zdHJ1Y3Rpb25zOiBzdHIpIC0+IGJvb2w6CiAgICAgICAgeCwgeSwgZHgsIGR5ID0gMCwgMCwgMCwgMQogICAgICAgIGZvciBpIGluIGluc3RydWN0aW9uczoKICAgICAgICAgICAgaWYgaSA9PSAnUic6IGR4LCBkeSA9IGR5LCAtZHgKICAgICAgICAgICAgaWYgaSA9PSAnTCc6IGR4LCBkeSA9IC1keSwgZHgKICAgICAgICAgICAgaWYgaSA9PSAnRyc6IHgsIHkgPSB4ICsgZHgsIHkgKyBkeQogICAgICAgIHJldHVybiAoeCwgeSkgPT0gKDAsIDApIG9yIChkeCwgZHkpICE9ICgwLDEp").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
