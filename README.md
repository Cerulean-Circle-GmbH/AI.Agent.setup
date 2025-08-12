# AI Agent Messaging System with A2A Gateway

A test-driven implementation of agent-to-agent communication using Google's A2A protocol principles, featuring a central Gateway server that manages agent registration, task routing, and message storage.

## Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Alice Agent   │    │  A2A Gateway    │    │   Bob Agent     │
│   (Port 8001)   │◄──►│   (Port 8000)   │◄──►│   (Port 8002)   │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## Folder Structure

```
AI.Agent.setup/
│
├── gateway/              # A2A Gateway server
│   └── a2a_gateway.py    # Central message broker
│
├── agents/               # All agent apps
│   ├── alice.py          # Alice's FastAPI app
│   ├── bob.py            # Bob's FastAPI app
│   ├── alice_prompt.md   # Alice's identity and instructions
│   └── bob_prompt.md     # Bob's identity and instructions
│
├── tests/                # All test files
│   ├── test_agents_messaging.py
│   └── test_agent.py
│
├── shared/               # Shared resources/utilities
│   └── message_store.py  # Legacy shared store (deprecated)
│
├── README.md             # Project documentation
├── package.json          # NPM scripts and dependencies
└── ...                   # Other project files
```

## Getting Started

### 1. Install Dependencies
```bash
npm install
```

### 2. Start the A2A Gateway Server
```bash
npm run start:gateway
```
This starts the central Gateway server on `http://localhost:8000`

### 3. Start the Agents
In separate terminals:
```bash
# Terminal 1: Start Alice
npm run start:alice

# Terminal 2: Start Bob  
npm run start:bob
```

Or start all services at once:
```bash
npm run start:all
```

### 4. Run Tests
```bash
npm run start  # Runs pytest on tests/
```

## API Endpoints

### Gateway (Port 8000)
- `GET /health` - Health check
- `GET /agents` - List registered agents
- `POST /agents/register` - Register an agent
- `POST /tasks` - Submit a task
- `GET /tasks/{task_id}` - Get task status
- `POST /messages` - Send a message
- `GET /messages?receiver={name}` - Get messages for receiver

### Alice (Port 8001)
- `POST /send` - Send message through Gateway
- `GET /messages?receiver={name}` - Get messages from Gateway
- `GET /health` - Health check

### Bob (Port 8002)
- `POST /send` - Send message through Gateway
- `GET /messages?receiver={name}` - Get messages from Gateway
- `GET /health` - Health check
- `GET /agent-card` - Bob's capabilities
- `POST /tasks` - Handle tasks (echo, reverse)

## Agent Communication Flow

1. **Registration**: Agents register with the Gateway on startup
2. **Messaging**: Agents send/receive messages through the Gateway
3. **Task Execution**: Background agents can receive and execute tasks
4. **Discovery**: Agents can discover each other's capabilities

## Integration with Cursor

This system can be integrated with Cursor's active chat and background agents by:
- Using the Gateway as a message broker between active and background agents
- Implementing MCP tools for the active chat to interact with the Gateway
- Following the A2A protocol for standardized agent communication

## Testing

The test suite verifies:
- Agent registration with the Gateway
- Message exchange between Alice and Bob
- Task execution capabilities
- API endpoint functionality

All tests should pass when the Gateway and agents are running.
