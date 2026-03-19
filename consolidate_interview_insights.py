#!/usr/bin/env python3
"""
Consolidate interview insights from folders 1-77 into the INSIGHTS folder.
Maps which interviews have been analyzed and which are missing insights.
"""

import os
import shutil
from pathlib import Path
import json
from datetime import datetime

# Configuration
BASE_PATH = Path(r"C:\Users\mtk17\OneDrive\Desktop\L2M\Lab2Market\Interviews")
INSIGHTS_PATH = BASE_PATH / "INSIGHTS"
INTERVIEWS_TO_CHECK = list(range(1, 78))  # 1-77

# Priority file patterns to look for
INSIGHT_FILE_PATTERNS = [
    "*Interview_Analysis.md",
    "*_Analysis.md",
    "Executive_Summary.md",
    "*Interview_Profile.md",
    "*_Profile.md",
    "insights.md",
]

def find_analysis_file(folder_path):
    """Find the main analysis file in a folder."""
    if not folder_path.exists():
        return None
    
    # Check for priority files
    for pattern in INSIGHT_FILE_PATTERNS:
        matches = list(folder_path.glob(pattern))
        if matches:
            return matches[0]
    
    return None

def check_if_in_insights(interview_num, folder_path):
    """Check if interview insights already exist in INSIGHTS folder."""
    if not folder_path.exists():
        return False, "Folder not found"
    
    # Find analysis file in original folder
    analysis_file = find_analysis_file(folder_path)
    if not analysis_file:
        return False, "No analysis file found"
    
    # Check if similar file exists in INSIGHTS
    file_name = analysis_file.name
    insights_file = INSIGHTS_PATH / file_name
    
    if insights_file.exists():
        return True, f"Found: {file_name}"
    
    return False, f"Missing: {file_name}"

def get_interview_name(folder_path):
    """Extract interview subject name from folder contents."""
    if not folder_path.exists():
        return "Unknown"
    
    # Look for profile or analysis file that contains subject name
    analysis_file = find_analysis_file(folder_path)
    if analysis_file:
        # Extract name from filename
        name = analysis_file.stem.replace("_Interview_Analysis", "").replace("_Analysis", "").replace("_Interview_Profile", "").replace("_Profile", "")
        return name
    
    return "Unknown"

def main():
    print("=" * 80)
    print("INTERVIEW INSIGHTS CONSOLIDATION AUDIT")
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 80)
    
    # Track results
    interviews_with_insights = []
    interviews_missing_insights = []
    folders_not_found = []
    
    # Check each interview
    for interview_num in INTERVIEWS_TO_CHECK:
        folder_path = BASE_PATH / str(interview_num)
        
        if not folder_path.exists():
            folders_not_found.append(interview_num)
            continue
        
        # Get interview details
        interview_name = get_interview_name(folder_path)
        is_in_insights, message = check_if_in_insights(interview_num, folder_path)
        analysis_file = find_analysis_file(folder_path)
        
        interview_info = {
            "interview_num": interview_num,
            "name": interview_name,
            "has_analysis_file": analysis_file is not None,
            "analysis_filename": analysis_file.name if analysis_file else None,
            "in_insights_folder": is_in_insights,
            "status_message": message
        }
        
        if is_in_insights:
            interviews_with_insights.append(interview_info)
        else:
            interviews_missing_insights.append(interview_info)
    
    # Print summary
    print(f"\n📊 SUMMARY")
    print(f"Total interviews checked: {len(INTERVIEWS_TO_CHECK)}")
    print(f"Folders found: {len(INTERVIEWS_TO_CHECK) - len(folders_not_found)}")
    print(f"With analysis files: {sum(1 for i in interviews_with_insights + interviews_missing_insights if i['has_analysis_file'])}")
    print(f"✓ Already in INSIGHTS folder: {len(interviews_with_insights)}")
    print(f"✗ Missing from INSIGHTS folder: {len(interviews_missing_insights)}")
    print(f"⚠ Folders not found: {folders_not_found if folders_not_found else 'None'}\n")
    
    # Show interviews WITH insights
    if interviews_with_insights:
        print("\n✓ INTERVIEWS WITH INSIGHTS (Already in INSIGHTS folder):")
        print("-" * 80)
        for info in sorted(interviews_with_insights, key=lambda x: x['interview_num']):
            print(f"  [{info['interview_num']:2d}] {info['name']:40s} - {info['status_message']}")
    
    # Show interviews MISSING insights
    if interviews_missing_insights:
        print("\n✗ INTERVIEWS MISSING INSIGHTS (Need consolidation):")
        print("-" * 80)
        for info in sorted(interviews_missing_insights, key=lambda x: x['interview_num']):
            if info['has_analysis_file']:
                print(f"  [{info['interview_num']:2d}] {info['name']:40s} - COPY: {info['analysis_filename']}")
            else:
                print(f"  [{info['interview_num']:2d}] {info['name']:40s} - NO ANALYSIS FILE")
    
    # Save detailed report
    report_data = {
        "generated_at": datetime.now().isoformat(),
        "summary": {
            "total_checked": len(INTERVIEWS_TO_CHECK),
            "folders_found": len(INTERVIEWS_TO_CHECK) - len(folders_not_found),
            "with_insights": len(interviews_with_insights),
            "missing_insights": len(interviews_missing_insights),
            "folders_not_found": folders_not_found
        },
        "with_insights": interviews_with_insights,
        "missing_insights": interviews_missing_insights
    }
    
    report_file = BASE_PATH / "INSIGHTS" / "consolidation_audit_report.json"
    with open(report_file, 'w') as f:
        json.dump(report_data, f, indent=2)
    
    print(f"\n📋 Detailed report saved to: consolidation_audit_report.json")
    
    # Generate action items
    print("\n" + "=" * 80)
    print("ACTION ITEMS:")
    print("=" * 80)
    
    copy_count = 0
    for info in interviews_missing_insights:
        if info['has_analysis_file']:
            copy_count += 1
            src = BASE_PATH / str(info['interview_num']) / info['analysis_filename']
            dest = INSIGHTS_PATH / info['analysis_filename']
            print(f"  [{copy_count}] Copy {info['analysis_filename']} from folder {info['interview_num']}")
    
    return interviews_missing_insights

if __name__ == "__main__":
    missing = main()
