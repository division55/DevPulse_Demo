import unittest
from agents.router import route_question
from agents.repository_agent import answer_repository_question

class DevPulseTests(unittest.TestCase):
    def test_repository_route(self):
        self.assertEqual(route_question("show repository info"), "repository")

    def test_issue_route(self):
        self.assertEqual(route_question("triage this bug"), "issue_triage")

    def test_release_route(self):
        self.assertEqual(route_question("show latest release"), "release")

    def test_repository_demo_data(self):
        result = answer_repository_question(
            "show repository info for octocat/Hello-World", live=False
        )
        self.assertIn("octocat/Hello-World", result)
        self.assertIn("local sample data", result)

if __name__ == "__main__":
    unittest.main()
