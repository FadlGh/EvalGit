import argparse
from core.log import log_evaluation
from core.db import get_all_evaluations, get_specific_row
from core.report import write_report

def main():
    parser = argparse.ArgumentParser(prog="evalgit", description="Local model evaluation tracker")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # log command
    log_parser = subparsers.add_parser("log", help="Log a new evaluation")
    log_parser.add_argument("--model", required=True)
    log_parser.add_argument("--gt", required=True)
    log_parser.add_argument("--pred", required=True)
    log_parser.add_argument("--dataset", required=True)
    log_parser.add_argument("--notes", default="")
    log_parser.add_argument("--report", required=False, action="store_true")

    # show command
    show_parser = subparsers.add_parser("show", help="Show evaluations")
    show_parser.add_argument("--key", choices=["id", "timestamp", "model_name", "dataset", "notes"])
    show_parser.add_argument("--value")

    args = parser.parse_args()

    if args.command == "log":
        metrics = log_evaluation(
            model_name=args.model,
            gt_file=args.gt,
            pred_file=args.pred,
            dataset_name=args.dataset,
            notes=args.notes,
        )
        print("Logged evaluation:")
        for k, v in metrics.items():
            print(f"{k}: {v}")
        if args.report:
            path = write_report(
                model_name=args.model,
                metrics=metrics,
                dataset=args.dataset,
                notes=args.notes,
            )
            print(f"Markdown report saved at {path}")

    elif args.command == "show":
        if args.key and args.value:
            row = get_specific_row(args.key, args.value)
            if row:
                print("Match Found:")
                print(row)
            else:
                print("No matching row found.")
        else:
            print("All evaluations:")
            for row in get_all_evaluations():
                print(row)

if __name__ == "__main__":
    main()
