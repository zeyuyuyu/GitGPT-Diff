# GitGPT-Diff

AI-Powered Git Diff Analysis & Automated Code Review Platform

## Overview
GitGPT-Diff revolutionizes code review by combining LLM technology with semantic Git diff analysis. It goes beyond traditional diff tools by understanding code context, detecting potential bugs, and suggesting architectural improvements in real-time.

## Key Features
- 🧠 Semantic understanding of code changes across commits
- 🔍 AI-powered vulnerability detection
- 📊 Impact analysis on system architecture
- 🤖 Automated PR summaries with risk assessment
- 🔄 Integration with major CI/CD platforms
- 📈 Technical debt tracking and recommendations

## Installation
```bash
pip install gitgpt-diff
```

## Usage
```bash
gitgpt-diff analyze --branch feature/new-auth
gitgpt-diff review --pr 123
```

## Configuration
```yaml
model: gpt-6-turbo
analysis_depth: deep
ignore_patterns:
  - '*.log'
  - 'node_modules/*'
```

## Requirements
- Python 3.11+
- OpenAI API key or compatible LLM
- Git 2.40+

## Contributing
Contributions welcome! See [CONTRIBUTING.md](CONTRIBUTING.md)

## License
MIT