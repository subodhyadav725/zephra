import argparse
from zephra.agent import ZephraAgent

def main():
    parser = argparse.ArgumentParser(description="Zephra Agentic Workflow Engine")
    parser.add_argument("--target", type=str, default=".", help="Directory or workspace path to analyze")
    parser.add_argument("--task", type=str, default="Perform code audit and optimization", help="Task instruction for the agent")
    parser.add_argument("--model", type=str, default="gpt-6-astra", help="Model tier to utilize")

    args = parser.parse_args()

    agent = ZephraAgent(model_name=args.model)
    result = agent.run_pipeline(target_path=args.target, instruction=args.task)

    print("\n--- Zephra Execution Result ---")
    for key, value in result.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()