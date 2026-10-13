"""DevPulse educational demo: route GitHub questions to a specialist handler."""
from agents.router import route_question
from agents.repository_agent import answer_repository_question

def main():
    print("=" * 58)
    print("DevPulse — GitHub Intelligence Assistant (Educational Demo)")
    print("=" * 58)
    print("Modes: demo (local sample data) or live (public GitHub API)")
    mode = input("Choose mode [demo/live]: ").strip().lower() or "demo"
    if mode not in {"demo", "live"}:
        print("Unknown mode. Starting in demo mode.")
        mode = "demo"

    print("\nExample: show repository info for octocat/Hello-World")
    question = input("Ask DevPulse: ").strip()
    if not question:
        question = "show repository info for octocat/Hello-World"

    intent = route_question(question)
    print(f"\n[Router] Selected specialist: {intent}")

    if intent == "repository":
        result = answer_repository_question(question, live=(mode == "live"))
    else:
        result = (
            "This small demo currently implements repository-information routing. "
            f"The question was classified as '{intent}'."
        )

    print("\n[DevPulse response]")
    print(result)

if __name__ == "__main__":
    main()
