import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--token", required=False)
args = parser.parse_args()

token = args.token
print(token)

if not token:
    print("No token provided")
    exit(1)
