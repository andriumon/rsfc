from rsfc.model import assessedSoftware as soft
from rsfc.model import indicator as ind
from rsfc.model import assessment as asmt
from rsfc.model import markdownReportGenerator as mdRep
from rsfc.harvesters import github_harvester as gt
from rsfc.utils import rsfc_helpers


def start_assessment(repo, branch, tag, ftr, test_id, token):
    
    print("Assessing repository...")

    indi = ind.Indicator(somef, gh) #Esto va a ser el Evaluator 
    checks = indi.assess_indicators(test_id)
    
    assess = asmt.Assessment(checks)
    badge_url = rsfc_helpers.generate_badge(checks)
    
    rsfc_asmt = assess.render_template(sw, ftr, test_id)
    table, info, badge = assess.to_terminal_table(test_id, badge_url)
    report = mdRep.MarkdownReportGenerator(rsfc_asmt, table)
    report.generate("./RSFC_REPORT.md")
    if test_id != None:
        table = table + info
    else:
        table = table + info + badge
    
    return rsfc_asmt, table
