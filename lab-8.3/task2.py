import unittest
# Function under test
def assign_grade(score):
    if not isinstance(score, (int, float)):
        return "Invalid input"
    if score < 0 or score > 100:
        return "Invalid score"
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
class TestAssignGrade(unittest.TestCase):
    # Valid A grade tests
    def test_grade_A_boundaries(self):
        self.assertEqual(assign_grade(100), "A")
        self.assertEqual(assign_grade(90), "A")
        self.assertEqual(assign_grade(95), "A")
    # Valid B grade tests
    def test_grade_B_boundaries(self):
        self.assertEqual(assign_grade(89), "B")
        self.assertEqual(assign_grade(80), "B")
        self.assertEqual(assign_grade(85), "B")
    # Valid C grade tests
    def test_grade_C_boundaries(self):
        self.assertEqual(assign_grade(79), "C")
        self.assertEqual(assign_grade(70), "C")
        self.assertEqual(assign_grade(75), "C")
    # Valid D grade tests
    def test_grade_D_boundaries(self):
        self.assertEqual(assign_grade(69), "D")
        self.assertEqual(assign_grade(60), "D")
        self.assertEqual(assign_grade(65), "D")
    # Valid F grade tests
    def test_grade_F(self):
        self.assertEqual(assign_grade(59), "F")
        self.assertEqual(assign_grade(0), "F")
        self.assertEqual(assign_grade(30), "F")
    # Invalid inputs
    def test_invalid_scores(self):
        self.assertEqual(assign_grade(-5), "Invalid score")
        self.assertEqual(assign_grade(105), "Invalid score")
        self.assertEqual(assign_grade("eighty"), "Invalid input")
        self.assertEqual(assign_grade(None), "Invalid input")
    # Float input test
    def test_float_input(self):
        self.assertEqual(assign_grade(72.5), "C")
if __name__ == "__main__":
    unittest.main()