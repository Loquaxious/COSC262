"""A program to display the output of the line_edits function in an
   html table.
   Written for COSC262 Assignment 1, Questions 3 and 4, 2020.
   Richard Lobb February 2020.
"""
import os
import re
from html import escape
import webbrowser
import sys

DEFAULT_CSS = """
table {font-size: 100%; border-collapse: collapse}
td, th  {border: 1px solid LightGrey; padding: 2px; }
td del {background-color: #FFBB00; text-decoration: none;}
"""

class HtmlTable:
    """A table to be rendered in HTML."""
    def __init__(self, column_headers):
        """The column headers is a list of strings. Its length determines the
           number of columns in the table"""
        self.headers = column_headers
        self.num_cols = len(column_headers)
        self._html = ""
        self._html += "<tr>" + ''.join(f"<th>{hdr}</th>" for hdr in column_headers) + "</tr>\n"

    def add_row(self, values, column_styles=None):
        """Given a list of strings ('values'), the length of which must match
           the length of the list of column headers when the table was created,
           add one row to the table. column_styles is an optional list of
           strings for setting the style attributes of the row's <td>
           elements. If given, its length must match the number of columns.

           For example
              add_row(["this", "that"], ["background-color:yellow", ""])

           would add a table row containing the values 'this' and 'that' with the
           first column having a background-color of yellow. An empty style
           string is ignored.
           String values are html-escaped (i.e. characters like '&' and '<' get
           converted to HTML-entities). Then, as a special feature for this
           assignment, any sequence of characters wrapped in double square
           brackets is instead wrapped in HTML <del> elements; these are by
           default rendered with a purple background by the HTML renderer.
           Then any newline characters are converted to <br>.
           Finally the resulting string is wrapped in a <pre> element.
        """
        def td_element(value, style, i_column):
            value = escape(value)  # HTML escaping
            value = re.sub(r'\[\[(..*?)\]\]', r'<del>\1</del>', value,
                flags=re.DOTALL + re.MULTILINE)
            value = value.replace('\n', '<br>')
            style_string = f' style="{style}"' if style else ''
            td = f"<td{style_string}><pre>{value}</pre></td>"
            return td

        if column_styles is None:
            column_styles = ["" for i in range(self.num_cols)]
        tds = [td_element(values[i], column_styles[i], i) for i in range(self.num_cols)]
        row = f"<tr>{''.join(tds)}</tr>\n"
        self._html += row

    def html(self):
        return "<table>\n" + self._html + "</table>\n"


class HtmlRenderer:
    """A class to help with displaying HTML for COSC262 Assignment 1, 2020.
       Once constructed"""
    def __init__(self, css=DEFAULT_CSS):
        """Initialise self to contain the given html string"""
        self.html = ''
        self.css = css

    def add_html(self, html):
        """Concatenate the given html to the end of the current html string"""
        self.html += html

    def render(self):
        """Display the current html in a browser window"""
        html = f"""<html><head><style>{self.css}</style></head><body>{self.html}</body></html>"""
        path = os.path.abspath('temp.html')
        with open(path, 'w') as f:
            f.write(html)
        webbrowser.open('file://' + path)


def edit_table(operations):
    """Construct an HtmlTable to display the given sequence of operations, as
       returned by the line_edits function.
    """
    table = HtmlTable(["Previous", "Current"])
    grey = "background-color:LightGrey"
    for op, left, right in operations:
        if op == 'C':
            table.add_row([left, right])
        elif op == 'D':
            table.add_row([left, right], ["background-color:#BBBBFF", grey])
        elif op == 'S':
            bg = "background-color:#FFFF99"
            table.add_row([left, right], [bg, bg])
        else:
            table.add_row([left, right], [grey, "background-color:#ABEBC6"])
    return table


#************************************************************************
#
def line_edits(s1, s2):
    """ Takes two strings as parameters representing the previous and current 
    versions of the code file. It uses the edit distance algorithm with whole 
    lines as the comparison elements, to determine which lines to delete, insert
    alter or just copy. The output will be a list of 3-element tuples 
    (op, left_line, right_line) that will correspond line for line wiht the 
    output table"""
    
    result = []
    split1 = s1.splitlines()
    split2 = s2.splitlines()
    n = len(split1) 
    m = len(split2)
    
    table = pop_table(split1, split2)
    
    while (n != 0 or m != 0):
        if n == 0 or m == 0:
            if n == 0 and m == 0:
                return result
            elif n == 0:
                result = [('I', '', split2[m-1])] + result
                m -= 1
            else:
                result = [('D', split1[n-1], '')] + result
                n -= 1
        elif split1[n-1] == split2[m-1]:
            result = [('C', split1[n-1], split2[m-1])] + result
            n -= 1
            m -= 1
        elif table[n-1][m-1] <= table[n-1][m] and table[n-1][m-1] <= table[n][m-1]:
            result = subs_line(split1[n-1], split2[m-1]) + result 
            n -= 1
            m -= 1        
        elif table[n-1][m] < table[n][m-1] and table[n-1][m] < table[n-1][m-1]:
            result = [('D', split1[n-1], '')] + result
            n -= 1
        elif table[n][m-1] < table[n-1][m] and table[n][m-1] < table[n-1][m-1]:
            result = [('I', '', split2[m-1])] + result
            m -= 1
    return result


def subs_line(line1, line2):
    """ If a subsitute operation happsn in the line edits method this is called
    to check mark what characters have been changed"""
    line_lcs1 = lcs(line1, line2)
    line_lcs2 = line_lcs1[:]
    result1 = ''
    result2 = ''
    
    for char1 in line1:
        if (line_lcs1 != None and line_lcs1 != '') and line_lcs1[0] == char1:
            result1 += line_lcs1[0]
            line_lcs1 = line_lcs1[1:]
        else:
            result1 += '[[' + char1 + ']]'
    
    for char2 in line2:
        if (line_lcs2 != None and line_lcs2 != '') and line_lcs2[0] == char2:
            result2 += line_lcs2[0]
            line_lcs2 = line_lcs2[1:]
        else:
            result2 += '[[' + char2 + ']]'
    
    return [('S', result1, result2)]

   
def lcs(s1, s2):
    """A Bottom Up approach to the lcs algorithm"""
    n1 = len(s1) + 1
    n2 = len(s2) + 1
    
    table = [[None for _ in range(n2)] for _ in range(n1)]
    
    for i in range(n1):
        for j in range(n2):
            if i == 0 or j == 0:
                table[i][j] = 0
            elif s1[i-1] == s2[j-1]:
                table[i][j] = table[i-1][j-1] + 1
            else:
                table[i][j] = max(table[i][j-1], table[i-1][j])
                
    n = len(s1) 
    m = len(s2) 
    result = ''
    while (table[n][m] != 0):
        if s1[n-1] == s2[m-1]:
            result = s1[n-1] + result
            n -= 1
            m -= 1
        else:
            if table[n-1][m] >= table[n][m-1]:
                n -= 1
            else:
                m -= 1
    
    return result


def pop_table(split1, split2):
    """Populates the table for the bottom up version of the edit distance 
    algorithm"""
    n1 = len(split1) + 1
    n2 = len(split2) + 1
    
    table = [[None for _ in range(n2)] for _ in range(n1)]
    
    for i in range(n1):
        for j in range(n2):
            if i == 0 and j == 0:
                table[i][j] = 0
            elif i == 0:
                table[i][j] = j
            elif j == 0:
                table[i][j] = i
            elif split1[i-1] == split2[j-1]:
                table[i][j] = table[i-1][j-1]
            else:
                table[i][j] = 1 + min(table[i-1][j], table[i][j-1], table[i-1][j-1])
    return table 
#
#************************************************************************


def main(s1, s2):
    renderer = HtmlRenderer()
    renderer.add_html("<h1>Show Differences (COSC262 2020)</h1>")
    operations = line_edits(s1, s2)
    table = edit_table(operations)
    renderer.add_html(table.html())
    renderer.render()

# Two example strings s1 and s2, follow.
# These are the same ones used in the assignment spec.

s1 = r'''# ============== DELETEs =====================
# TODO: add docstrings
@app.route('/queue/<hostname>', methods=['DELETE'])
def delete(hostname):
    try:
        data = json.loads(request.get_data())
        mac_address = data['macAddress']
    except:
        abort(400, 'Missing or invalid user data')
    status = queue.dequeue(hostname, macAddress)
    return ('', status)


@app.route('/queue', methods=['DELETE'])
def empty_queue():
    if request.remote_addr.upper() != TUTOR_MACHINE.upper():
        abort(403, "Not authorised")
    else:
        queue.clear_queue()
        response = jsonify({"message": "Queue emptied"})
        response.status_code = 204
        return response
'''

s2 = r'''# ============== DELETEs =====================
@app.route('/queue/<hostname>', methods=['DELETE'])
def delete(hostname):
    """Handle delete request from the given host"""
    try:
        data = json.loads(request.get_data())
        mac_address = data['mac_address']
    except:
        abort(400, 'Missing or invalid user data')
    status = queue.dequeue(hostname, mac_address)
    return ('', status)


@app.route('/queue', methods=['DELETE'])
def clear_queue():
    """Clear the queue. Valid only if coming from tutor machine"""
    if request.remote_addr.upper() != TUTOR_MACHINE.upper():
        abort(403, "Only the tutor machine can clear the queue")
    else:
        queue.clear_queue()
        response = jsonify({"message": "Queue cleared"})
        response.status_code = 204
        return response
'''

main(s1, s2)
