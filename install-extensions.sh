#!/bin/bash
mkdir -p .vscode
cat << 'EOF' >.vscode/settings.json
{
    "python.testing.unittestArgs":["-v","-s","./src/test","-p","*test*.py"],
    "python.testing.pytestEnabled": false,
    "python.testing.unittestEnabled":true,
    "extensions.ignoreRecommendations": true
}
EOF
cat << 'EOF' > .git/hooks/post-commit
#!/bin/bash
git push
git log -1 --shortstat > history_log.txt
EOF
chmod +x .git/hooks/post-commit
# code --install-extension local-rev.local-python-rev