import argparse
import json
from calibratemockup import run


def parse_args():
    parser = argparse.ArgumentParser(description="calibratemockup")
    parser.add_argument(
        "--estimations",
        dest="estimations",
        type=str,
        required=True,
        help="JSON array of estimation values",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    try:
        estimations = json.loads(args.estimations)
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Invalid JSON for --estimations: {exc}")

    if not isinstance(estimations, list):
        raise SystemExit("The --estimations argument must be a JSON array.")

    result = run(estimations)
    print(json.dumps(result))


if __name__ == "__main__":
    main()
