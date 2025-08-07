# Research Agent Setup Guide

This guide will help you set up and use the Research Agent that implements the WODA methodology (What, Overview, Details, Actions).

## Quick Start

### Option 1: Python (Recommended - No Dependencies Required)

The Python version is ready to use immediately:

```bash
# Navigate to the AI.Agent.setup directory
cd /Users/Shared/EAMD.ucp/md-wiki/AI.Agent.setup

# Run the research agent
python3 research_agent.py
```

### Option 2: Node.js (Full API Server)

If you have Node.js installed:

```bash
# Install dependencies
npm install

# Start the server
npm start

# Or use the startup script
./start.sh
```

#### Installing Node.js

If Node.js is not installed, you can install it using:

**macOS (using Homebrew):**
```bash
# Install Homebrew first (if not installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Node.js
brew install node
```

**macOS (using official installer):**
1. Download from https://nodejs.org/
2. Run the installer
3. Verify installation: `node --version`

**Linux (Ubuntu/Debian):**
```bash
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt-get install -y nodejs
```

**Windows:**
1. Download from https://nodejs.org/
2. Run the installer
3. Verify installation: `node --version`

## Project Structure

```
AI.Agent.setup/
├── src/
│   └── index.js              # Node.js server implementation
├── research_agent.py         # Python implementation (standalone)
├── client.js                 # Node.js client for testing
├── research/                 # Generated research folders
├── .cursor/                  # Cursor agent configuration
│   ├── agent-config.json     # Agent configuration
│   ├── agent-state.json      # Agent state tracking
│   ├── environment.json      # Background agent environment
│   └── scripts/              # Agent management scripts
│       └── agent-manager.js  # Agent lifecycle management
├── package.json              # Node.js dependencies
├── .cursorrules             # Cursor IDE integration
├── README.md               # Main documentation
├── SETUP.md               # This setup guide
├── start.sh               # Startup script
└── research.agent.md      # Original specification
```

## Features

### WODA Methodology Implementation
- **What**: Define topic, scope, and core concepts
- **Overview**: Document current knowledge vs. research needs
- **Details**: Collect and document research findings
- **Actions**: Derive actionable insights and next steps

### Automatic File Generation
For each research question, the agent creates:
- Topic file with the question
- Research task list
- WODA framework files (what.md, overview.md, details.md, actions.md)
- Answer.md (when research is complete)

### Cursor Integration
The `.cursorrules` file configures Cursor IDE to:
- Recognize research questions
- Automatically create research structures
- Follow WODA methodology
- Maintain organized documentation

## Usage Examples

### Python Version

```python
from research_agent import ResearchAgent

# Create agent
agent = ResearchAgent()

# Process a research question
question = "Can Cursor automate backend agent creation?"
result = agent.process_research_request(question)
print(f"Created research: {result['topic_name']}")

# Get research status
status = agent.get_research_status(result['topic_name'])
print(f"Status: {status['status']}")

# Update research
updates = {
    'what.md': '# What\n\n## Topic Definition\nCursor automation capabilities...',
    'overview.md': '# Overview\n\n## What We Know\nCursor can generate files...'
}
agent.update_research(result['topic_name'], updates)

# Create final answer
answer = {
    'question': question,
    'summary': 'Yes, Cursor can automate backend agent creation...',
    'details': 'Detailed explanation...',
    'actions': 'Recommended implementation steps...',
    'references': 'Sources and links...'
}
agent.create_answer(result['topic_name'], answer)
```

### Node.js Version (API)

```bash
# Start the server
npm start

# Create research (using curl)
curl -X POST http://localhost:3000/research \
  -H "Content-Type: application/json" \
  -d '{"question": "Can Cursor automate backend agent creation?"}'

# Get research status
curl http://localhost:3000/research/can-cursor-automate-backend-agent-creation

# List all research
curl http://localhost:3000/research
```

## Research File Structure

Each research topic creates this structure:

```
research/
└── topic-name/
    ├── topic-name.md          # Main topic file with question
    ├── research-tasks.md      # Comprehensive task list
    ├── what.md               # WODA: What
    ├── overview.md           # WODA: Overview  
    ├── details.md            # WODA: Details
    ├── actions.md            # WODA: Actions
    └── answer.md             # Final comprehensive answer
```

## Cursor Integration

The `.cursorrules` file enables Cursor to:
1. **Recognize Research Questions**: Automatically detect when you're asking for research
2. **Create Structures**: Generate organized research folders
3. **Follow WODA**: Maintain consistent methodology
4. **Track Progress**: Update status and documentation

### .cursor Folder Structure

The `.cursor` folder contains the agent configuration and management:

```
.cursor/
├── agent-config.json     # Agent configuration and settings
├── agent-state.json      # Agent state and session tracking
├── environment.json      # Background agent environment configuration
└── scripts/
    └── agent-manager.js  # Agent lifecycle management
```

#### Environment Configuration

The `environment.json` file configures the Cursor background agent environment:

- **Install Commands**: `npm install` to set up dependencies
- **Terminal Sessions**: Multiple terminal configurations for different agent functions
- **Environment Variables**: Development settings and port configuration
- **Package Requirements**: Node.js and Python version specifications
- **Feature Flags**: Research agent capabilities and settings

### Agent Management Commands

Once Node.js is installed, you can use these npm scripts:

```bash
# Activate the research agent
npm run agent:activate

# Deactivate the research agent
npm run agent:deactivate

# Check agent status
npm run agent:status

# Create new research
npm run agent:create "Your research question here"
```

Or use the agent manager directly:

```bash
# Activate agent
node .cursor/scripts/agent-manager.js activate

# Create research
node .cursor/scripts/agent-manager.js create "Can Cursor automate backend agents?"

# Check status
node .cursor/scripts/agent-manager.js status
```

### Using with Cursor

1. **Ask a Research Question**: Simply ask any question in Cursor
2. **Agent Responds**: Creates research structure automatically
3. **Follow WODA**: Fill in the generated files
4. **Complete Research**: Create final answer

## Development

### Adding Features

#### Python Version
- Extend the `ResearchAgent` class in `research_agent.py`
- Add new methods as needed
- Update the main function for testing

#### Node.js Version
- Extend the `ResearchAgent` class in `src/index.js`
- Add new API endpoints
- Update client.js for testing

### Testing

```bash
# Python version
python3 research_agent.py

# Node.js version
npm test
```

## Troubleshooting

### Python Issues
- **Permission Denied**: Run `chmod +x research_agent.py`
- **Module Not Found**: Python 3 is required

### Node.js Issues
- **npm not found**: Install Node.js from https://nodejs.org/
- **Port in use**: Change PORT in src/index.js or use different port

### General Issues
- **Files not created**: Check write permissions in the directory
- **Research not found**: Verify topic name spelling

## Next Steps

1. **Customize**: Modify the WODA templates to match your needs
2. **Extend**: Add new research methodologies
3. **Integrate**: Connect with external research tools
4. **Automate**: Set up automated research workflows

## Support

- Check the README.md for detailed documentation
- Review the original research.agent.md specification
- Test with the provided examples
- Modify the code to fit your specific needs

The Research Agent is now ready to help you conduct structured research following the WODA methodology!

## Related Files

- **[Research Agent Project Summary](PROJECT_SUMMARY.md)**
- **[Research Agent Setup](README.md)**
- **[Research Agent Definition](research.agent.md)**
- **[Actions](research/can-cursor-automate-the-creation/actions.md)**
- **[Can Cursor Automate The Creation](research/can-cursor-automate-the-creation/can-cursor-automate-the-creation.md)**
- **[Details](research/can-cursor-automate-the-creation/details.md)**
- **[Overview](research/can-cursor-automate-the-creation/overview.md)**
- **[Research Tasks for: Can Cursor automate the creation of a backend agent like you?](research/can-cursor-automate-the-creation/research-tasks.md)**
- **[What](research/can-cursor-automate-the-creation/what.md)**
- **[Cursor Background Agents Research](research/cursor-background-agents/0_topic.md)**
- **[What: Cursor Background Agents](research/cursor-background-agents/1_what.md)**
- **[Cursor Background Agents: Comprehensive Analysis](research/cursor-background-agents/2_answer.md)**
- **[Access & Control: Cursor Background Agents](research/cursor-background-agents/access-control.md)**
- **[Actions: Cursor Background Agents Implementation Guide](research/cursor-background-agents/actions.md)**
- **[Implementation Guide: Cursor Background Agents](research/cursor-background-agents/implementation-guide.md)**
- **[Operational Considerations: Cursor Background Agents](research/cursor-background-agents/operational-considerations.md)**
- **[Overview: Cursor Background Agents Research Hub](research/cursor-background-agents/overview.md)**
- **[Research Tasks: Cursor Background Agents](research/cursor-background-agents/research-tasks.md)**
- **[Security & Privacy: Cursor Background Agents](research/cursor-background-agents/security-privacy.md)**
- **[Technical Architecture: Cursor Background Agents](research/cursor-background-agents/technical-architecture.md)**
