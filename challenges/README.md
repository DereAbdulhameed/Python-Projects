# Python Challenge Repository 🐍

Welcome to the Python Challenge Repository! Test your Python programming skills with various challenges and get instant automated feedback.

## 🎯 How It Works

1. **Choose a Challenge**: Browse the `challenges/` directory and pick a challenge
2. **Read the Task**: Each challenge has a detailed description and requirements
3. **Write Your Solution**: Implement your solution in the designated file
4. **Submit**: Push your code or create a pull request
5. **Get Feedback**: Automated tests will run and provide instant feedback on your solution

## 📁 Repository Structure

```
challenges/
├── 01_dna_sequence/          # DNA sequence manipulation challenge
│   ├── README.md             # Challenge description
│   ├── solution.py           # Your solution goes here
│   ├── test_solution.py      # Automated tests
│   └── examples.py           # Example inputs/outputs
├── 02_next_challenge/
│   └── ...
└── ...
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- pytest (for running tests locally)

### Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd Python-Projects
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Quick Start Example

Let's solve your first challenge step-by-step:

1. **Navigate to a challenge**:
   ```bash
   cd challenges/01_dna_sequence
   ```

2. **Read the challenge**: Open `README.md` to understand the task

3. **Open the solution file**: Edit `solution.py` - this is where you write your code
   ```python
   # You'll see function templates like this:
   def validate_dna(sequence: str) -> bool:
       pass  # Replace 'pass' with your implementation
   ```

4. **Implement your solution**: Replace `pass` with your code
   ```python
   def validate_dna(sequence: str) -> bool:
       valid_chars = set('ATGCatgc')
       return all(char in valid_chars for char in sequence)
   ```

5. **Test your solution**:
   ```bash
   pytest test_solution.py -v
   ```

6. **See results**: Green = passed ✅, Red = failed ❌

**Important**: Only edit `solution.py` - don't modify test files or create new files!

### Running Tests Locally

Navigate to a challenge directory and run:
```bash
pytest challenges/01_dna_sequence/test_solution.py -v
```

Or run all tests:
```bash
pytest challenges/ -v
```

## 📝 Submission Methods

### Method 1: Direct Push (For Collaborators)
```bash
git add .
git commit -m "Solution for DNA sequence challenge"
git push
```

### Method 2: Pull Request (Recommended for Contributors)
1. Fork the repository
2. Create a new branch: `git checkout -b solution/your-name-challenge-name`
3. Implement your solution
4. Push to your fork
5. Create a Pull Request
6. Automated tests will run on your PR

## ✅ Automated Testing

When you submit your solution:
- ✨ Tests run automatically via GitHub Actions
- 📊 You'll see a ✅ or ❌ status on your commit/PR
- 📝 Detailed test results show what passed/failed
- 🎯 Score is calculated based on test coverage

## 🏆 Challenge Levels

- 🟢 **Beginner**: Basic Python syntax and logic
- 🟡 **Intermediate**: Data structures and algorithms
- 🔴 **Advanced**: Complex algorithms and optimization

## 📚 Available Challenges

1. **DNA Sequence** (🟢 Beginner) - String manipulation and basic algorithms

More challenges coming soon!

## 🤝 Contributing

Want to add a new challenge? Follow the template in `challenge_template/` and submit a PR!

## 📖 Rules

- Write clean, readable code
- Follow PEP 8 style guidelines
- Don't modify test files
- Your solution should pass all tests
- No external libraries unless specified in the challenge

## 💡 Tips

- Read the challenge description carefully
- Check the example inputs/outputs
- Run tests locally before submitting
- Start with simple test cases
- Optimize after getting it working

## 📫 Support

If you have questions or find issues, please open an issue on GitHub.

Happy Coding! 🚀
