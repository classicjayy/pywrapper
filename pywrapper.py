import sys

def exit(args=None):
  if args:
    sys.exit(f"{args}")
  else:
    logging.exit("ExitError: no syntax provided.")

def playground(args2=None):
  if args2:
    exec(f"{args2}")
  else:
    logging.exit("ExecError: no syntax provided.")
