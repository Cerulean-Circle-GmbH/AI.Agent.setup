**🔙 Back to**: [Topic](./0_topic.md) | [Overview](./overview.md)

# Technical Architecture: Cursor Background Agents

## Remote Environment Setup {#remote-environment}

### Base Infrastructure
**Ubuntu-based Virtual Machines**: Each agent runs in its own isolated VM
- **AWS Infrastructure**: Hosted on Amazon Web Services
- **Resource Isolation**: No shared resources between agents
- **Internet Access**: Full connectivity for package installation and research
- **Scalability**: Multiple agents can run concurrently

### Package Management
**Universal Package Support**: Can install any required dependencies
- **Ubuntu Packages**: Full access to apt package manager
- **Language-Specific**: npm (Node.js), pip (Python), gem (Ruby), etc.
- **Development Tools**: Compilers, debuggers, IDEs, and utilities
- **Custom Software**: Any software available for Ubuntu Linux

### State Persistence
**Optimized Startup Performance**
- **Disk State Caching**: Environment state cached after install commands
- **Fast Initialization**: Subsequent startups use cached state
- **Session-Based**: State persists only during agent session
- **Automatic Cleanup**: Resources cleaned up after completion

## Environment Configuration {#configuration}

### environment.json Specification
**Central Configuration File**: Located at `.cursor/environment.json`

```json
{
  "snapshot": "POPULATED_FROM_SETTINGS",
  "install": "npm install && pip install -r requirements.txt",
  "start": "sudo service docker start",
  "terminals": [
    {
      "name": "Development Server",
      "command": "npm run dev"
    },
    {
      "name": "Test Runner", 
      "command": "npm run test:watch"
    }
  ]
}
```

### Configuration Components

#### Snapshot Management
- **Base Environment**: Identifier for the base environment state
- **Version Control**: Tracks environment configurations
- **Reusability**: Can be shared across team members

#### Install Commands
**Dependency Installation**: Run before agent starts
- **Idempotent Design**: Safe to run multiple times
- **Caching Strategy**: Results cached for fast subsequent startups
- **Multi-Language Support**: Can combine multiple package managers
- **Build Processes**: Can include compilation and build steps

#### Startup Commands
**Environment Initialization**: Optional post-install setup
- **Service Management**: Start required services (Docker, databases)
- **Environment Variables**: Set runtime configuration
- **System Preparation**: Initialize development environment

#### Terminal Sessions
**Background Processes**: Managed via tmux sessions
- **Development Servers**: Long-running processes (web servers, APIs)
- **Build Watchers**: Continuous compilation and testing
- **Shared Access**: Both user and agent can access sessions
- **Process Management**: Automatic restart and monitoring

## Repository Integration {#repository-integration}

### GitHub Connection
**Primary Git Provider**: Full integration with GitHub
- **Authentication**: OAuth-based secure connection
- **Read-Write Access**: Full repository permissions required
- **Submodule Support**: Handles dependent repositories
- **Organization Support**: Works with GitHub organizations

### Branch Management
**Automatic Branch Operations**
- **Isolated Development**: Each agent works on separate branch
- **Automatic Creation**: Branches created for agent work
- **Push Operations**: Changes pushed back to repository
- **Merge Integration**: Easy integration with main branch

### Repository Operations
**Full Git Functionality**
- **Clone Operations**: Automatic repository cloning
- **File Modifications**: Edit any files in repository
- **Commit Management**: Automatic commits with descriptive messages
- **History Preservation**: Full git history maintained

### Future Provider Support
**Planned Integrations**
- **GitLab**: Full GitLab integration planned
- **BitBucket**: BitBucket support in development
- **Self-Hosted**: Support for enterprise Git servers
- **Version Control Systems**: Potential support for other VCS

## Advanced Configuration {#advanced-configuration}

### Dockerfile Support
**Custom Environment Setup**: Advanced system-level configuration

```dockerfile
FROM ubuntu:22.04

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    nodejs \
    docker.io

# Install specific compiler versions
RUN apt-get install -y gcc-11 g++-11

# Configure development tools
RUN npm install -g typescript@latest
```

#### Dockerfile Best Practices
- **Base Image Selection**: Choose appropriate Ubuntu version
- **System Dependencies**: Install required system packages
- **Development Tools**: Include necessary compilers and debuggers
- **No Project Copy**: Workspace managed separately from Docker
- **Dependency Separation**: Use install commands for project dependencies

### Custom Environment Setup
**Advanced Development Environments**
- **IDE Integration**: Connect IDE instances to remote machines
- **Tool Installation**: Install specific development tools
- **Environment Snapshots**: Save configured environments for reuse
- **Team Standardization**: Consistent environments across team

### Process Management
**Advanced Process Control**

#### Install Phase
- **Dependency Resolution**: Handle complex dependency trees
- **Build Optimization**: Efficient compilation and building
- **Error Handling**: Robust error recovery and reporting
- **Progress Monitoring**: Real-time installation progress

#### Runtime Phase
- **Service Management**: Start and monitor required services
- **Resource Monitoring**: Track CPU, memory, and disk usage
- **Health Checks**: Monitor process health and availability
- **Auto-Recovery**: Automatic restart of failed processes

## Performance Optimization

### Startup Performance
**Fast Environment Initialization**
- **Cached Dependencies**: Pre-installed common packages
- **Optimized Images**: Lightweight base images
- **Parallel Processing**: Concurrent installation and setup
- **Resource Pre-allocation**: Efficient resource management

### Runtime Performance
**Optimized Execution Environment**
- **Resource Scaling**: Dynamic resource allocation
- **Network Optimization**: Efficient network connectivity
- **Storage Performance**: Fast SSD storage for all operations
- **Monitoring Integration**: Real-time performance metrics

### Resource Management
**Efficient Resource Utilization**
- **Memory Management**: Optimal memory allocation
- **CPU Scheduling**: Efficient CPU utilization
- **Storage Optimization**: Minimal disk space usage
- **Network Efficiency**: Optimized network operations

---

**🔗 Related Topics**:
- [Security & Privacy](./security-privacy.md) - Security aspects of the technical architecture
- [Access & Control](./access-control.md) - How users interact with the technical infrastructure
- [Implementation Guide](./implementation-guide.md) - Practical setup and configuration steps