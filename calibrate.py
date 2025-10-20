import argparse
import json
from calibratemockup import run


def parse_args():
    parser = argparse.ArgumentParser(description="calibratemockup")
    parser.add_argument(
        "--measurements",
        dest="measurements",
        type=str,
        required=True,
        help="JSON array of estimation values",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    try:
        measurements = json.loads(args.measurements)
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Invalid JSON for --measurements: {exc}")

    if not isinstance(measurements, list):
        raise SystemExit("The --measurements argument must be a JSON array.")

    result = run(measurements)
    print(json.dumps(result))


if __name__ == "__main__":
    main()
