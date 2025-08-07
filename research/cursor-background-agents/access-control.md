**🔙 Back to**: [Topic](./0_topic.md) | [Overview](./overview.md)

# Access & Control: Cursor Background Agents

## User Interface {#user-interface}

### Background Agent Sidebar
**Native Cursor Integration**: Primary agent management interface
- **Agent List**: View all agents associated with your account
- **Search Functionality**: Find agents by name, status, or project
- **Creation Interface**: Start new agents directly from sidebar
- **Status Monitoring**: Real-time status updates and progress indicators
- **Quick Actions**: Stop, restart, or access agents with one click

#### Sidebar Features
- **Filtering Options**: Filter agents by status (running, completed, failed)
- **Sorting Capabilities**: Sort by creation date, last activity, or status
- **Visual Indicators**: Clear status icons and progress bars
- **Context Menu**: Right-click options for common agent operations

### Background Agent Mode
**Keyboard-Triggered Interface**: Ctrl+E for quick agent access
- **Agent Selection**: Choose from list of available agents
- **Status Viewing**: Monitor current agent progress and activities
- **Machine Access**: Direct access to remote agent environment
- **Follow-up Prompts**: Send additional instructions to running agents

#### Mode Features
- **Quick Navigation**: Fast switching between different agents
- **Command Interface**: Direct command execution on remote machines
- **Real-time Updates**: Live streaming of agent activities and outputs
- **Intervention Controls**: Ability to pause, modify, or stop agent actions

## Agent Operation {#agent-operation}

### Asynchronous Execution
**Independent Agent Operation**: Agents work without constant user input
- **Background Processing**: Agents continue working while user is away
- **Autonomous Decision Making**: Agents can make development decisions independently
- **Multi-tasking**: Can handle multiple tasks simultaneously
- **Persistent Sessions**: Work continues across user sessions

### Auto-Execution Capabilities
**Automatic Command Execution**: Differs from foreground agents
- **No User Approval**: Commands execute automatically without confirmation
- **Test Automation**: Automatic running of tests and validation
- **Iterative Development**: Can fix issues and retry automatically
- **Continuous Integration**: Seamless integration with development workflows

#### Execution Features
- **Command History**: Complete log of all executed commands
- **Output Capture**: Full capture of command outputs and results
- **Error Handling**: Automatic error detection and recovery attempts
- **Performance Monitoring**: Real-time monitoring of execution performance

### Real-time Monitoring
**Live Agent Supervision**: Continuous oversight of agent activities
- **Activity Streams**: Real-time feed of agent actions and decisions
- **Progress Indicators**: Visual progress bars and completion percentages
- **Status Updates**: Immediate notification of status changes
- **Intervention Points**: Clear indicators when user intervention may be needed

#### Monitoring Features
- **Detailed Logs**: Comprehensive logging of all agent activities
- **Performance Metrics**: CPU, memory, and network usage statistics
- **Error Tracking**: Real-time error detection and reporting
- **Alert System**: Notifications for important events or issues

## Machine Access and Control

### Remote Environment Access
**Direct Machine Interaction**: Full access to agent's working environment
- **Shell Access**: Direct command-line interface to agent's machine
- **File System Access**: Browse and edit files in the remote environment
- **Process Management**: Monitor and control running processes
- **Network Access**: Full network connectivity from remote machine

### tmux Session Management
**Shared Terminal Sessions**: Both user and agent can access terminals
- **Session Persistence**: Terminal sessions persist across connections
- **Multiple Windows**: Support for multiple terminal windows and panes
- **Shared Control**: Both user and agent can interact with same session
- **Session Recovery**: Reconnect to existing sessions after disconnection

#### tmux Features
- **Window Management**: Create, switch, and manage multiple windows
- **Pane Splitting**: Split windows into multiple panes for efficiency
- **Session Naming**: Name sessions for easy identification and access
- **Scrollback Buffer**: Access to command history and output

### File and Directory Operations
**Comprehensive File Management**: Full file system access and control
- **File Editing**: Edit any files in the remote environment
- **Directory Navigation**: Browse and manage directory structures
- **File Transfer**: Upload and download files to/from remote machine
- **Permission Management**: Control file and directory permissions

## Intervention and Handoff

### User Intervention Capabilities
**Real-time Control Override**: Take control at any time
- **Immediate Stop**: Instantly halt agent execution
- **Command Injection**: Execute commands while agent is running
- **Task Redirection**: Change agent focus or priorities
- **Manual Override**: Take manual control of any operation

### Handoff Procedures
**Seamless Transition**: Easy transfer between agent and human work
- **Context Preservation**: Maintain full context during handoff
- **State Transfer**: Complete transfer of working state and environment
- **Documentation**: Automatic documentation of agent work and decisions
- **Resume Capability**: Restart agent work after human intervention

#### Handoff Features
- **Work Summary**: Detailed summary of agent accomplishments
- **Next Steps**: Clear identification of remaining tasks
- **Issue Documentation**: Record of any problems or challenges encountered
- **Recommendation Engine**: Suggestions for next actions or improvements

## Status and Communication

### Status Tracking System
**Comprehensive Agent Status Management**
- **Current Activity**: Real-time indication of what agent is doing
- **Progress Tracking**: Percentage completion and time estimates
- **Health Monitoring**: System health and resource usage indicators
- **Error States**: Clear indication of errors or issues

#### Status Types
- **Running**: Agent actively working on tasks
- **Waiting**: Agent waiting for resources or dependencies
- **Completed**: Task completion with success indicators
- **Failed**: Error states with diagnostic information
- **Paused**: User-initiated pause or intervention

### Communication Channels
**Multi-channel Agent Communication**
- **Real-time Chat**: Direct communication with running agents
- **Status Updates**: Automatic notifications of important events
- **Progress Reports**: Regular updates on agent progress and activities
- **Error Notifications**: Immediate alerts for errors or issues

### Follow-up and Feedback
**Continuous Agent Interaction**
- **Additional Instructions**: Send new tasks or modifications to running agents
- **Clarification Requests**: Respond to agent questions or requests for guidance
- **Feedback Loop**: Provide feedback on agent performance and decisions
- **Course Correction**: Adjust agent direction based on results

## Team Collaboration

### Multi-user Access
**Collaborative Agent Management**
- **Shared Agents**: Multiple team members can access same agent
- **Permission Control**: Granular control over who can access which agents
- **Concurrent Access**: Multiple users can monitor agent simultaneously
- **Handoff Between Users**: Transfer agent control between team members

### Team Visibility
**Organization-wide Agent Transparency**
- **Team Dashboard**: Overview of all team agents and their status
- **Activity Feed**: Team-wide feed of agent activities and accomplishments
- **Resource Usage**: Team-level resource usage and cost tracking
- **Performance Analytics**: Team performance metrics and insights

### Collaboration Features
**Enhanced Team Productivity**
- **Agent Sharing**: Share agents and their work with team members
- **Knowledge Transfer**: Automatic documentation of agent learnings
- **Best Practices**: Shared library of successful agent configurations
- **Team Templates**: Standardized agent setups for common tasks

---

**🔗 Related Topics**:
- [Technical Architecture](./technical-architecture.md) - Infrastructure supporting access and control
- [Security & Privacy](./security-privacy.md) - Security aspects of access control
- [Implementation Guide](./implementation-guide.md) - Setting up access and control systems