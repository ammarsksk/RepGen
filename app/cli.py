import argparse
from app.graph.nodes import researcher, outliner, writer, reviewer, finalizer
from app.graph.runner import run_pipeline, state_summary


def main():
    p = argparse.ArgumentParser(prog = "agentic-writer")
    sub = p.add_subparsers(dest="cmd", required=True)
    run_p = sub.add_parser("run", help="Run the pipeline")
    run_p.add_argument("--topic", required=True)
    args = p.parse_args()

    if args.cmd == "run":
        nodes = [researcher, outliner, writer, reviewer, finalizer]
        state = run_pipeline(topic=args.topic, nodes=nodes)
        print(state_summary(state))

