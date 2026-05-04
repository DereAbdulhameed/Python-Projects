# Contributing to Python Challenge Repository

Thank you for your interest in contributing! 🎉

## How to Submit Your Solution

### For Participants (Solving Challenges)

1. **Fork the repository** (if you don't have write access)

2. **Clone your fork**:
   ```bash
   git clone https://github.com/YOUR_USERNAME/Python-Projects.git
   cd Python-Projects
   ```

3. **Create a new branch**:
   ```bash
   git checkout -b solution/your-name-challenge-name
   # Example: git checkout -b solution/john-dna-sequence
   ```

4. **Navigate to the challenge**:
   ```bash
   cd challenges/01_dna_sequence
   ```

5. **Implement your solution** in `solution.py`

6. **Test locally**:
   ```bash
   pytest test_solution.py -v
   ```

7. **Commit and push**:
   ```bash
   git add solution.py
   git commit -m "Add solution for DNA sequence challenge"
   git push origin solution/your-name-challenge-name
   ```

8. **Create a Pull Request** on GitHub
   - The automated tests will run automatically
   - You'll see the results in the PR checks
   - Green checkmark ✅ means all tests passed!

### For Challenge Creators (Adding New Challenges)

Want to contribute a new challenge? Great! Follow this structure:

1. **Create a new challenge directory**:
   ```
   challenges/XX_challenge_name/
   ├── README.md           # Challenge description
   ├── solution.py         # Template with function signatures
   ├── test_solution.py    # Comprehensive tests
   └── examples.py         # Example usage (optional)
   ```

2. **Challenge README should include**:
   - Clear problem description
   - Difficulty level (🟢 Beginner, 🟡 Intermediate, 🔴 Advanced)
   - Function signatures and requirements
   - Example inputs/outputs
   - Hints and learning objectives

3. **Write comprehensive tests**:
   - Cover edge cases
   - Test invalid inputs
   - Include multiple test scenarios
   - Use descriptive test names

4. **Test your challenge**:
   - Implement a working solution
   - Verify all tests pass
   - Remove your solution before submitting

5. **Submit a PR** with:
   - Challenge description
   - Why this challenge is valuable
   - Estimated difficulty and time

## Code Style Guidelines

- Follow PEP 8 style guide
- Use type hints where appropriate
- Write clear docstrings
- Keep functions focused and simple
- Add comments for complex logic

## Testing Guidelines

- Use pytest for all tests
- Organize tests into classes by function
- Test edge cases (empty inputs, large inputs, etc.)
- Use descriptive test names: `test_function_name_scenario`

## Questions?

Open an issue if you have questions or need help!

Happy coding! 🚀
