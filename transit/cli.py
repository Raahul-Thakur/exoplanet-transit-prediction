import argparse
from exoplanet_transit.pipelines.synthetic_demo import run

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--demo", default="synthetic")
    args = parser.parse_args()

    if args.demo == "synthetic":
        run()

if __name__ == "__main__":
    main()
