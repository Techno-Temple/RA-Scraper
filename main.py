import argparse

from launch import launch


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Launch scraping")
    parser.add_argument(
        "--config-file", type=str, default=None, help="Path to config file"
    )
    args = parser.parse_args()
    launch(args)
