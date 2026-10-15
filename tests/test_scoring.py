import unittest

from resume_lens.scoring import compare_texts
from resume_lens.skills import find_skills


class ResumeLensTests(unittest.TestCase):
    def test_similarity_is_bounded(self):
        result = compare_texts("Python developer using pandas", "Python developer using pandas")
        self.assertGreaterEqual(result["similarity"], 0.0)
        self.assertLessEqual(result["similarity"], 1.0)

    def test_empty_text_is_rejected(self):
        with self.assertRaises(ValueError):
            compare_texts("", "A job description")

    def test_skill_detection(self):
        skills = find_skills("Built projects using Python, SQL, and Docker.")
        self.assertIn("python", skills)
        self.assertIn("sql", skills)
        self.assertIn("docker", skills)
        self.assertNotIn("kubernetes", skills)


if __name__ == "__main__":
    unittest.main()
