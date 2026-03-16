import argparse

class ROIEvaluator:
    """
    Translates ML metrics into executive-level financial projections.
    Ideal for Technical Sales and Client Engineering discussions.
    """
    def __init__(self, baseline_cost_per_failure: float, cost_per_inspection: float):
        self.baseline_cost = baseline_cost_per_failure
        self.inspection_cost = cost_per_inspection

    def calculate_business_value(self, true_positives, false_positives, false_negatives):
        # Value gained by preventing a failure
        savings_from_tp = true_positives * self.baseline_cost
        
        # Cost wasted on inspecting false alarms
        wasted_on_fp = false_positives * self.inspection_cost
        
        # Cost incurred from missed failures
        loss_from_fn = false_negatives * self.baseline_cost

        net_savings = savings_from_tp - wasted_on_fp
        
        return {
            "Total Prevented Losses": savings_from_tp,
            "Cost of False Alarms": wasted_on_fp,
            "Net AI Savings": net_savings
        }

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Strategic ROI Evaluator")
    parser.add_argument("--tp", type=int, default=120, help="True Positives (Correctly predicted failures)")
    parser.add_argument("--fp", type=int, default=15, help="False Positives (False alarms)")
    parser.add_argument("--fn", type=int, default=5, help="False Negatives (Missed failures)")
    args = parser.parse_args()

    # Assuming a federal aerospace or energy context
    evaluator = ROIEvaluator(baseline_cost_per_failure=250000, cost_per_inspection=5000)
    metrics = evaluator.calculate_business_value(args.tp, args.fp, args.fn)

    print("==================================================")
    print("📈 EXECUTIVE SUMMARY: AI STRATEGY & ROI PROJECTION")
    print("==================================================")
    for k, v in metrics.items():
        print(f"{k:25}: ${v:,.2f}")
    print("==================================================")
