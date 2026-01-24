#!/bin/bash
#
# Install Git hooks for Hanuman Chalisa project
#

echo "Installing Git hooks..."

# Copy pre-commit hook
if [ -f ".git/hooks/pre-commit" ]; then
    echo "✓ Pre-commit hook already exists"
else
    echo "✗ Pre-commit hook not found!"
    echo "  Hook should be at: .git/hooks/pre-commit"
    exit 1
fi

# Make executable
chmod +x .git/hooks/pre-commit
echo "✓ Pre-commit hook is executable"

echo ""
echo "🎉 Git hooks installed successfully!"
echo ""
echo "The pre-commit hook will now:"
echo "  • Validate YAML syntax in all verse files"
echo "  • Run Jekyll build to catch errors"
echo "  • Check for common issues"
echo "  • Prevent commits if validation fails"
echo ""
echo "To skip the hook (not recommended):"
echo "  git commit --no-verify"
echo ""
