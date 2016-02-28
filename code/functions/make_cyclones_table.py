def make_cyclones_table(x):
    """Creates a latex table stored in a python list
    
    Parameteres
    -----------
        x: dictionary
    
    Returns
    -------
        latex_tbl: latex table in a list
    """
    latex_tbl = []
    latex_tbl.append("\\begin{center}\n")
    latex_tbl.append("  \\begin{tabular}{ c c }\n")
    latex_tbl.append("    \\hline\n")
    latex_tbl.append("    Season & Count \\\\\n")
    latex_tbl.append("    \\hline\n")    
    # add data
    for key, value in x.items():
        latex_tbl.append("    %s & %s \\\\\n" % (key, str(value)))
    # close table
    latex_tbl.append("    \\hline\n")
    latex_tbl.append("  \\end{tabular}\n")
    latex_tbl.append("\\end{center}\n")
    return latex_tbl
