import argparse
from .log import log_evaluation
from .db import *
from .report import write_report

def main():
    init_db()
    parser = argparse.ArgumentParser(prog="evalgit", description="Local model evaluation tracker")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # log
    log_parser = subparsers.add_parser("log", help="Log a new evaluation")
    log_parser.add_argument("--model", required=True)
    log_parser.add_argument("--gt", required=True)
    log_parser.add_argument("--pred", required=True)
    log_parser.add_argument("--dataset", required=True)
    log_parser.add_argument("--notes", default="")
    log_parser.add_argument("--report", required=False, action="store_true")

    # show
    show_parser = subparsers.add_parser("show", help="Show evaluation(s)")
    show_parser.add_argument("--key", choices=["id", "timestamp", "model_name", "dataset", "notes"])
    show_parser.add_argument("--value")

    # delete
    delete_parser = subparsers.add_parser("delete", help="Delete evaluation(s)")
    delete_parser.add_argument("--key", choices=["id", "timestamp", "model_name", "dataset", "notes"])
    delete_parser.add_argument("--value")

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
            rows = get_all_evaluations()
            if not rows:
                print("DB is empty")
            else:
                print("All evaluations:")
                for row in rows:
                    print(row)

    elif args.command == "delete":
        if args.key and args.value:
            row = get_specific_row(args.key, args.value)
            if row:
                print("Match found:")
                print(row)
                confirm = input("Delete this row? (y/n): ").strip().lower()
                if confirm == "y":
                    delete_specific_row(args.key, args.value)
                    print("Row deleted.")
                else:
                    print("Aborted.")
            else:
                print("No matching row found.")
        else:
            confirm = input("Are you sure you want to delete ALL evaluations? (y/n): ").strip().lower()
            if confirm == "y":
                delete_all_rows()
                print("All rows deleted.")
            else:
                print("Aborted.")

if __name__ == "__main__":
    main()
