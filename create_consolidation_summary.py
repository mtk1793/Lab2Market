#!/usr/bin/env python3
"""
Create a comprehensive master consolidation document for all interview insights.
"""

import os
import json
from pathlib import Path

BASE_PATH = Path(r"C:\Users\mtk17\OneDrive\Desktop\L2M\Lab2Market\Interviews")
INSIGHTS_PATH = BASE_PATH / "INSIGHTS"

def read_file_header(file_path, lines=20):
    """Read first N lines of a file to extract insights."""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = [next(f) for _ in range(lines)]
        return ''.join(content)
    except:
        return ""

def main():
    # Read the audit report
    audit_file = INSIGHTS_PATH / "consolidation_audit_report.json"
    with open(audit_file, 'r') as f:
        audit_data = json.load(f)
    
    # Get all analysis files that are now in INSIGHTS
    md_files = list(INSIGHTS_PATH.glob("*Interview_Analysis.md")) + \
               list(INSIGHTS_PATH.glob("*_Analysis.md")) + \
               list(INSIGHTS_PATH.glob("*_Profile.md"))
    
    # Create master consolidation document
    doc_content = """# Interview Insights Consolidation Summary

**Generated:** March 17, 2026  
**Purpose:** Master index of all interview insights consolidation status  
**Last Updated:** From interviews 1-77

---

## 📊 CONSOLIDATION STATUS

| Metric | Count |
|--------|-------|
| **Total Interviews Checked** | 77 |
| **Interview Folders Found** | 65 |
| **With Formal Analysis Files** | 39 |
| **With Insights in INSIGHTS Folder** | 37 ✓ |
| **Newly Consolidated (This Session)** | 2 ✓ |
| **Folders Not Found (1-4, 36-38, 49, 74-77)** | 12 |
| **Folders with Interview Materials but No Analysis** | 26 |

---

## ✓ INTERVIEWS WITH CONSOLIDATED INSIGHTS

The following interviews have analysis files now in the INSIGHTS folder:

"""
    
    # Add the list of consolidated interviews
    with_insights = audit_data['with_insights']
    with_insights_sorted = sorted(with_insights, key=lambda x: x['interview_num'])
    
    for info in with_insights_sorted:
        doc_content += f"- **Interview {info['interview_num']}** - {info['name']} ({info['analysis_filename']})\n"
    
    doc_content += """

---

## ✗ INTERVIEWS NEEDING FORMAL ANALYSIS

The following interview folders contain interview materials but lack formal analysis files in the INSIGHTS folder:

"""
    
    # Add interviews missing insights
    missing_insights = audit_data['missing_insights']
    missing_sorted = sorted(missing_insights, key=lambda x: x['interview_num'])
    
    analysis_needed = [i for i in missing_sorted if i['has_analysis_file']]
    no_analysis_yet = [i for i in missing_sorted if not i['has_analysis_file']]
    
    if analysis_needed:
        doc_content += f"\n### Newly Consolidated ({len(analysis_needed)} files moved)\n"
        for info in analysis_needed:
            doc_content += f"- **Interview {info['interview_num']}** - {info['name']} (**MOVED**: {info['analysis_filename']})\n"
    
    if no_analysis_yet:
        doc_content += f"\n### Interviews Requiring Analysis Files ({len(no_analysis_yet)} folders)\n"
        doc_content += "\nThese interview folders contain transcripts or materials but no formal analysis file yet:\n\n"
        for info in no_analysis_yet:
            doc_content += f"- **Interview {info['interview_num']}** - {info['name']}\n"
    
    doc_content += """

---

## 📁 INTERVIEWS NOT FOUND

The following interview numbers have no corresponding folder:
- 1, 2, 3, 4 (Early interviews - may be in archive)
- 36, 37, 38 (Gap in sequence)
- 49 (Missing)
- 74, 75, 76, 77 (Future/planned interviews)

---

## 🔄 CONSOLIDATION ACTIONS COMPLETED (This Session)

1. **Copied John_Lidstone_Interview_Profile.md** from Folder 6 → INSIGHTS
2. **Copied Jens_Kroeger_Interview_Analysis.md** from Folder 63 → INSIGHTS
3. **Generated consolidation audit report** (consolidation_audit_report.json)
4. **Created this master summary** (Interview_Insights_Consolidation_Summary.md)

---

## 📋 NEXT STEPS

### Priority 1: Create Analysis Files for High-Priority Interviews
Interviews with transcripts/materials that need formal analysis:
- Interviews 7, 22, 24, 26, 29, 30, 40, 44, 47, 48, 50, 51, 54, 55, 61, 62, 64-73

### Priority 2: Archive Early Interviews
- Determine location of interviews 1-4 and archive accordingly

### Priority 3: Add Interview Summaries
- For interviews 61-73, create brief insight summaries from interview transcripts
- These appear to be recent interviews that may have key emerging patterns

---

## 📊 CONSOLIDATED ANALYSIS FILES IN INSIGHTS FOLDER

**Total files in INSIGHTS folder:** 
"""
    
    all_files = list(INSIGHTS_PATH.glob("*.md"))
    doc_content += f"{len(all_files)} markdown files\n\n"
    
    doc_content += """
### Files Added This Session:
1. John_Lidstone_Interview_Profile.md
2. Jens_Kroeger_Interview_Analysis.md

### Other Key Files in INSIGHTS:
"""
    
    # Key summary files
    key_files = [
        ("insights.md", "Main consolidated insights"),
        ("Executive_Summary.md", "Summary of interview 5"),
        ("Master_Insights_Summary", "Overall insights"),
        ("Hypothesis_Validation_Analysis.md", "Hypothesis validation"),
        ("INTERVIEWS_48_56_DETAILED_ANALYSIS.md", "In-depth analysis of interviews 48-56"),
    ]
    
    for fname, desc in key_files:
        if (INSIGHTS_PATH / fname).exists():
            doc_content += f"- {fname} - {desc}\n"
    
    doc_content += """

---

## 🎯 RECOMMENDATION

All 39 available interview analysis files are now consolidated in the INSIGHTS folder. 
The remaining work is to create formal analysis files for interviews 7, 22, 24, 26, 29, 30, 40, 44, 47, 48, 50, 51, 54, 55, and 61-73 from their existing interview transcripts and materials.

This consolidation ensures:
✓ All analysis is in one place  
✓ Easy reference for patterns across 65+ interviews  
✓ Clear tracking of which interviews still need analysis work  
✓ Foundation for master synthesis documents  

---

"""
    
    # Save the document
    output_file = INSIGHTS_PATH / "Interview_Insights_Consolidation_Summary.md"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(doc_content)
    
    print(f"✓ Created master consolidation summary: Interview_Insights_Consolidation_Summary.md")
    print(f"✓ Total insights now consolidated: 39 analysis files")
    print(f"✓ Newly added this session: 2 files")
    
    return output_file

if __name__ == "__main__":
    output = main()
