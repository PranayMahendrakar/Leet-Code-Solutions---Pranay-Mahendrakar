#!/usr/bin/env python3
"""
LeetCode Solutions Exporter to GitHub
Author: Pranay Mahendrakar
Usage: python leetcode_exporter.py
"""

import requests
import json
import os
import time
from pathlib import Path


class LeetCodeExporter:
    def __init__(self, cookies: str):
        self.session = requests.Session()
        self.session.headers.update({
            'Cookie': cookies,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Content-Type': 'application/json',
        })
        self.base_url = "https://leetcode.com"
        self.graphql_url = f"{self.base_url}/graphql"

    def get_all_submissions(self, limit=20, offset=0):
        """Fetch submissions using GraphQL API"""
        query = """
        query submissionList($offset: Int!, $limit: Int!) {
            submissionList(offset: $offset, limit: $limit) {
                lastKey
                hasNext
                submissions {
                    id
                    statusDisplay
                    lang
                    runtime
                    timestamp
                    url
                    memory
                    title
                    titleSlug
                }
            }
        }
        """
        response = self.session.post(self.graphql_url, json={
            'query': query,
            'variables': {'offset': offset, 'limit': limit}
        })
        return response.json()

    def get_submission_detail(self, submission_id: int):
        """Get the actual code of a submission"""
        query = """
        query submissionDetails($submissionId: Int!) {
            submissionDetails(submissionId: $submissionId) {
                code
                lang {
                    name
                    verboseName
                }
                question {
                    questionId
                    title
                    titleSlug
                    difficulty
                }
            }
        }
        """
        response = self.session.post(self.graphql_url, json={
            'query': query,
            'variables': {'submissionId': submission_id}
        })
        return response.json()

    def get_extension(self, lang: str) -> str:
        """Map language to file extension"""
        extensions = {
            'python': 'py', 'python3': 'py', 'java': 'java',
            'cpp': 'cpp', 'c': 'c', 'javascript': 'js',
            'typescript': 'ts', 'go': 'go', 'rust': 'rs',
            'kotlin': 'kt', 'swift': 'swift', 'scala': 'scala',
            'ruby': 'rb', 'php': 'php', 'csharp': 'cs',
        }
        return extensions.get(lang.lower(), 'txt')

    def export_solutions(self, output_dir: str = "leetcode-solutions"):
        """Export all accepted solutions"""
        base_path = Path(output_dir)
        base_path.mkdir(exist_ok=True)

        # Create difficulty folders
        for difficulty in ['Easy', 'Medium', 'Hard']:
            (base_path / difficulty.lower()).mkdir(exist_ok=True)

        offset = 0
        limit = 20
        exported = set()
        total_exported = 0

        print("🚀 Starting LeetCode export...")

        while True:
            print(f"📥 Fetching submissions (offset: {offset})...")
            result = self.get_all_submissions(limit=limit, offset=offset)

            if 'data' not in result or not result['data']['submissionList']:
                print("❌ Error fetching submissions. Check your cookies.")
                break

            submissions = result['data']['submissionList']['submissions']
            has_next = result['data']['submissionList']['hasNext']

            for sub in submissions:
                # Only export accepted solutions, one per problem
                if sub['statusDisplay'] != 'Accepted':
                    continue
                if sub['titleSlug'] in exported:
                    continue

                print(f"  📝 Exporting: {sub['title']}")

                # Get full submission details
                time.sleep(0.5)  # Rate limiting
                detail = self.get_submission_detail(int(sub['id']))

                if 'data' not in detail or not detail['data']['submissionDetails']:
                    continue

                details = detail['data']['submissionDetails']
                code = details['code']
                question = details['question']
                difficulty = question['difficulty'].lower()
                question_id = question['questionId']

                # Create filename
                ext = self.get_extension(sub['lang'])
                filename = f"{question_id.zfill(4)}-{sub['titleSlug']}.{ext}"
                filepath = base_path / difficulty / filename

                # Add header comment
                header = f"""# Problem: {question['title']}
# Difficulty: {question['difficulty']}
# URL: https://leetcode.com/problems/{sub['titleSlug']}/
# Runtime: {sub['runtime']}
# Memory: {sub['memory']}

"""
                # Write file
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(header + code)

                exported.add(sub['titleSlug'])
                total_exported += 1

            if not has_next:
                break
            offset += limit
            time.sleep(1)  # Rate limiting between batches

        # Create README
        self.create_readme(base_path, total_exported)
        print(f"\n✅ Exported {total_exported} solutions to '{output_dir}/'")
        return total_exported

    def create_readme(self, base_path: Path, total: int):
        """Generate a README.md file"""
        readme = f"""# LeetCode Solutions

📊 **Total Problems Solved:** {total}

## Structure
```
├── easy/       # Easy problems
├── medium/     # Medium problems
└── hard/       # Hard problems
```

## Progress
| Difficulty | Count |
|------------|-------|
| Easy       | {len(list((base_path / 'easy').glob('*')))} |
| Medium     | {len(list((base_path / 'medium').glob('*')))} |
| Hard       | {len(list((base_path / 'hard').glob('*')))} |

---
*Auto-generated using LeetCode Exporter*
"""
        with open(base_path / 'README.md', 'w') as f:
            f.write(readme)


def main():
    print("=" * 50)
    print("   LeetCode Solutions Exporter to GitHub")
    print("=" * 50)
    print()
    print("How to get your cookies:")
    print("1. Go to leetcode.com and log in")
    print("2. Open DevTools (F12) → Network tab")
    print("3. Refresh the page")
    print("4. Click any request → Headers → Cookie")
    print("5. Copy the entire cookie value")
    print()

    cookies = input("Paste your LeetCode cookies: ").strip()

    if not cookies:
        print("❌ No cookies provided. Exiting.")
        return

    exporter = LeetCodeExporter(cookies)
    exporter.export_solutions()

    print("\n📤 Next steps to push to GitHub:")
    print("   cd leetcode-solutions")
    print("   git init")
    print("   git add .")
    print('   git commit -m "Add LeetCode solutions"')
    print("   git remote add origin https://github.com/YOUR_USERNAME/leetcode-solutions.git")
    print("   git push -u origin main")


if __name__ == "__main__":
    main()