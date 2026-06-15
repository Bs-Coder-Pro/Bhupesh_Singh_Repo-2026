from pathlib import Path


class ReadmeGenerator:

    def __init__(
        self,
        project_name: str,
        description: str,
        author: str,
        version: str = "v1.0.0"
    ):

        self.project_name = project_name
        self.description = description
        self.author = author
        self.version = version

    def generate(self) -> str:

        readme = f"""# {self.project_name}

## Description

{self.description}

**Version:** {self.version}

---

## Features

- Voice Commands
- File Management
- Task Management
- Error Handling
- Logging System

---

## Installation

    pip install -r requirements.txt

---

## Usage

    python main.py

---

## Author

{self.author}

---

## License

MIT License
"""

        return readme

    def save(
        self,
        filename: str = "README.md"
    ) -> str:

        content = self.generate()

        Path(filename).write_text(
            content,
            encoding="utf-8"
        )

        return f"{filename} generated successfully."


generator = ReadmeGenerator(
      project_name="JARVIS AI Assistant",
      description="A modular AI assistant built with Python.",
      author="Bs_Coder_Pro"
)

print(generator.save())