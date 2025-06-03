from core.log import log_evaluation

if __name__ == "__main__":
    # Replace with actual test files you have
    model_id = "test_model_v2"
    gt_file = "test_data/ground_truth.json"
    pred_file = "test_data/predictions.json"
    dataset_name = "test_dataset"

    metrics = log_evaluation(model_id, gt_file, pred_file, dataset_name, "this is a test")
    print("Logged metrics:", metrics)
