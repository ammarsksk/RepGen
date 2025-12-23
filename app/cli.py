import argparse

def main():
    p = argparse.ArgumentParser(prog = "agentic-writer")
    p.add_argument("--topic", default = "Test topic", help = "Topic for the pipeline")
    args = p.parse_args()
    print(f"Agentic writer booted, Topic = {args.topic}")
