#!/bin/bash
# Auto Cross-Link Script for New Markdown Files
# Automatically runs cross-linking agent when new .md files are created

set -e

RESEARCH_DIR="${1:-research}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CROSSLINK_AGENT="$SCRIPT_DIR/crosslink_agent.py"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

log() {
    echo -e "${BLUE}[CrossLink]${NC} $1"
}

success() {
    echo -e "${GREEN}[CrossLink]${NC} $1"
}

warning() {
    echo -e "${YELLOW}[CrossLink]${NC} $1"
}

error() {
    echo -e "${RED}[CrossLink]${NC} $1"
}

# Check if Python script exists
if [[ ! -f "$CROSSLINK_AGENT" ]]; then
    error "Cross-link agent not found at: $CROSSLINK_AGENT"
    exit 1
fi

# Check if research directory exists
if [[ ! -d "$RESEARCH_DIR" ]]; then
    error "Research directory not found: $RESEARCH_DIR"
    exit 1
fi

# Function to process a single file
process_file() {
    local file_path="$1"
    log "Processing new markdown file: $file_path"
    
    if python3 "$CROSSLINK_AGENT" --research-dir "$RESEARCH_DIR" --file "$file_path"; then
        success "Cross-links updated for: $file_path"
    else
        error "Failed to update cross-links for: $file_path"
        return 1
    fi
}

# Function to process all files
process_all() {
    log "Processing all markdown files in $RESEARCH_DIR"
    
    if python3 "$CROSSLINK_AGENT" --research-dir "$RESEARCH_DIR" --report; then
        success "All cross-links updated successfully"
        success "Cross-link report generated"
    else
        error "Failed to update cross-links"
        return 1
    fi
}

# Function to watch for new files (requires fswatch)
watch_mode() {
    log "Starting watch mode for new markdown files..."
    
    if command -v fswatch >/dev/null 2>&1; then
        fswatch -0 -r --include='\.md$' "$RESEARCH_DIR" | while read -d '' file; do
            if [[ -f "$file" ]] && [[ "$file" == *.md ]]; then
                sleep 2  # Wait a bit for file to be fully written
                process_file "$file"
            fi
        done
    elif command -v inotifywait >/dev/null 2>&1; then
        inotifywait -m -r -e create --format '%w%f' "$RESEARCH_DIR" | while read file; do
            if [[ "$file" == *.md ]]; then
                sleep 2  # Wait a bit for file to be fully written
                if [[ -f "$file" ]]; then
                    process_file "$file"
                fi
            fi
        done
    else
        error "File watching requires fswatch (macOS) or inotifywait (Linux)"
        error "Install with: brew install fswatch (macOS) or apt-get install inotify-tools (Linux)"
        exit 1
    fi
}

# Function to setup automation
setup_automation() {
    log "Setting up automatic cross-linking..."
    
    # Create a simple file watcher script
    cat > "$SCRIPT_DIR/crosslink_watcher.sh" << 'EOF'
#!/bin/bash
# Crosslink Watcher - runs in background
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
exec "$SCRIPT_DIR/auto_crosslink.sh" watch >> "$SCRIPT_DIR/crosslink.log" 2>&1
EOF
    
    chmod +x "$SCRIPT_DIR/crosslink_watcher.sh"
    
    # Create launchd plist for macOS
    if [[ "$OSTYPE" == "darwin"* ]]; then
        local plist_path="$HOME/Library/LaunchAgents/com.crosslink.agent.plist"
        cat > "$plist_path" << EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.crosslink.agent</string>
    <key>ProgramArguments</key>
    <array>
        <string>$SCRIPT_DIR/crosslink_watcher.sh</string>
    </array>
    <key>WorkingDirectory</key>
    <string>$SCRIPT_DIR</string>
    <key>KeepAlive</key>
    <true/>
    <key>StandardOutPath</key>
    <string>$SCRIPT_DIR/crosslink.log</string>
    <key>StandardErrorPath</key>
    <string>$SCRIPT_DIR/crosslink_error.log</string>
</dict>
</plist>
EOF
        
        success "Created launchd service at: $plist_path"
        log "To start: launchctl load $plist_path"
        log "To stop: launchctl unload $plist_path"
    fi
    
    # Create systemd service for Linux
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        local service_path="$HOME/.config/systemd/user/crosslink-agent.service"
        mkdir -p "$(dirname "$service_path")"
        
        cat > "$service_path" << EOF
[Unit]
Description=Crosslink Agent for Markdown Files
After=graphical-session.target

[Service]
Type=simple
ExecStart=$SCRIPT_DIR/crosslink_watcher.sh
WorkingDirectory=$SCRIPT_DIR
Restart=always
RestartSec=5

[Install]
WantedBy=default.target
EOF
        
        success "Created systemd service at: $service_path"
        log "To start: systemctl --user enable crosslink-agent.service"
        log "To enable on boot: systemctl --user enable crosslink-agent.service"
    fi
    
    success "Automation setup complete!"
}

# Main script logic
case "${1:-}" in
    "watch")
        watch_mode
        ;;
    "setup")
        setup_automation
        ;;
    "all")
        process_all
        ;;
    "file")
        if [[ -z "$2" ]]; then
            error "Usage: $0 file <path_to_markdown_file>"
            exit 1
        fi
        process_file "$2"
        ;;
    "help"|"-h"|"--help")
        echo "Cross-Link Agent Automation Script"
        echo ""
        echo "Usage:"
        echo "  $0 [command] [options]"
        echo ""
        echo "Commands:"
        echo "  all                    Process all markdown files"
        echo "  file <path>           Process single markdown file"
        echo "  watch                 Watch for new files and process automatically"
        echo "  setup                 Setup automatic cross-linking service"
        echo "  help                  Show this help message"
        echo ""
        echo "Options:"
        echo "  Research directory can be specified as first argument (default: research)"
        echo ""
        echo "Examples:"
        echo "  $0 all                                    # Process all files in research/"
        echo "  $0 all /path/to/research                 # Process all files in custom dir"
        echo "  $0 file research/topic/new-file.md      # Process single file"
        echo "  $0 watch                                 # Start watching for new files"
        echo "  $0 setup                                 # Setup automatic service"
        ;;
    *)
        log "Processing all markdown files (use 'help' for more options)"
        process_all
        ;;
esac