import os
import sys
import git
from typing import List, Dict

class GitDiff:
    def __init__(self, repo_path: str):
        self.repo = git.Repo(repo_path)

    def get_diff_with_context(self, commit_sha: str = None) -> Dict:
        """Get git diff with additional context and summary"""
        if commit_sha:
            # Get diff between commit and its parent
            diff = self.repo.commit(commit_sha).parents[0].diff(commit_sha)
        else:
            # Get working directory changes
            diff = self.repo.index.diff(None)

        changes = {
            'files_changed': [],
            'total_additions': 0,
            'total_deletions': 0,
            'summary': ''
        }

        for d in diff:
            file_diff = {
                'file': d.a_path,
                'change_type': d.change_type,
                'additions': d.diff.count(b'+'),
                'deletions': d.diff.count(b'-'),
                'content': d.diff.decode('utf-8')
            }
            changes['files_changed'].append(file_diff)
            changes['total_additions'] += file_diff['additions']
            changes['total_deletions'] += file_diff['deletions']

        # Generate summary
        changes['summary'] = f"Changed {len(changes['files_changed'])} files with "\
                           f"{changes['total_additions']} additions and "\
                           f"{changes['total_deletions']} deletions"

        return changes

    def get_file_history(self, filepath: str, num_commits: int = 5) -> List[Dict]:
        """Get commit history for a specific file"""
        history = []
        for commit in self.repo.iter_commits(paths=filepath, max_count=num_commits):
            history.append({
                'sha': commit.hexsha,
                'author': commit.author.name,
                'date': commit.committed_datetime.isoformat(),
                'message': commit.message.strip()
            })
        return history

def main():
    if len(sys.argv) < 2:
        print("Please provide repository path")
        sys.exit(1)

    repo_path = sys.argv[1]
    if not os.path.exists(repo_path):
        print(f"Repository path {repo_path} does not exist")
        sys.exit(1)

    diff_tool = GitDiff(repo_path)
    
    # Example usage
    changes = diff_tool.get_diff_with_context()
    print(f"\nDiff Summary:\n{changes['summary']}\n")
    
    for file_change in changes['files_changed']:
        print(f"File: {file_change['file']}")
        print(f"Type: {file_change['change_type']}")
        print(f"Changes: +{file_change['additions']} -{file_change['deletions']}")
        print("\nDiff Content:")
        print(file_change['content'])
        print("-" * 80)

if __name__ == "__main__":
    main()
