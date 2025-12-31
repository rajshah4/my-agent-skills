# My Agent Skills

A collection of reusable skills for AI coding assistants (Claude Code, Cursor, Windsurf, etc.)

## What are Skills?

Skills are modular, reusable prompts that extend AI assistant capabilities. Each skill is a self-contained unit that can be invoked when relevant to the task at hand.

## Installation

### For Claude Code

This repository is designed to work seamlessly with Claude Code via symlink:

```bash
# Clone the repository
git clone https://github.com/rajshah4/my-agent-skills.git ~/Code/my-agent-skills

# Create symlink to Claude's skills directory
ln -s ~/Code/my-agent-skills/skills ~/.claude/skills

# Restart Claude Code to load skills
```

### For Other AI Assistants

Copy the skills to your assistant's configuration directory or reference them as needed.

## Available Skills

Skills are organized in the `skills/` directory. Each skill contains:
- `SKILL.md` - The skill definition with YAML metadata and instructions
- Supporting files as needed

Currently includes skills from [Hamel Husain's collection](https://github.com/hamelsmu/hamel/tree/main/skills):
- `annotate-talk` - Annotate talks with timestamps
- `gem` - Generate educational materials
- `kit` - Starter kit for new projects
- `youtube-chapters` - Create chapter markers for YouTube videos
- `youtube-transcribe` - Transcribe YouTube videos
- `zoom` - Process Zoom recordings

## Adding Your Own Skills

1. Create a new directory in `skills/` with your skill name
2. Add a `SKILL.md` file with this structure:

```yaml
---
name: your-skill-name
description: What this skill does and when to use it
---

# Your Skill Title

## Instructions
Your detailed instructions here...
```

3. Commit and push:

```bash
git add skills/your-skill-name
git commit -m "Add your-skill-name skill"
git push
```

4. Restart your AI assistant to load the new skill

## Syncing Across Machines

Since this is a Git repository, you can sync skills across multiple machines:

```bash
cd ~/Code/my-agent-skills
git pull
```

Your AI assistant will automatically pick up the changes after restart.

## Contributing

Feel free to add new skills or improve existing ones. Each skill should:
- Be self-contained and modular
- Have clear, concise instructions
- Include examples where helpful
- Work across different AI assistants when possible

## Credits

Initial skills sourced from [Hamel Husain's skills collection](https://github.com/hamelsmu/hamel/tree/main/skills).

## License

MIT
