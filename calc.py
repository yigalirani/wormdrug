
def calc(name,kg,mg_per_kg,concetration_pct):
  dose_in_mg=mg_per_kg*kg
  concetration=concetration_pct/100
  paste_mg=dose_in_mg/concetration
  paste_grams=paste_mg/1000
  return locals()
def calc_iver(name,kg):
  return calc(name,kg,.2,1.78)
def calc_guard(name,kg):
  return calc(name,kg,9,10)

def make_row(tds):
  return  f"<tr>{'\n'.join(tds)}</tr>"

def format_input_to_string(var):
    """
    Accepts a variable that can be a string or a float.

    - If the input is a string, it returns the string as is.
    - If the input is a float, it converts the float to a string 
      formatted to 4 decimal places.
    
    Args:
        var (str or float): The input variable.

    Returns:
        str: The formatted string representation of the input.
    """
    if isinstance(var, str):
        # If it's a string, return it as is
        return var
    elif isinstance(var, float):
        # If it's a float, convert it to a string with 4 decimal places
        # The f-string format specifier ':.4f' handles this
        return f"{var:.4f}"
    else:
        # Handle other types gracefully (e.g., integers, booleans)
        # For simplicity, we'll convert them to a standard string
        # You can adjust this 'else' block based on specific needs
        return str(var)
def make_data_row(row,cols):
  ans=[]
  for col in cols:
    val=format_input_to_string(row[col])
    ans.append(f"<td>{val}</td>")
  return make_row(ans)

def make_rows(data,cols):
  ans=[]
  for row in data:
    ans.append(make_data_row(row,cols))
  return '\n'.join(ans)

def make_header(cols):
  ans=[]
  for col in cols:
    ans.append(f"<th>{col.replace('_', ' ')}</th>")
  return make_row(ans)

def make_table(data,title):
  cols=data[0].keys()
  header=make_header(cols)
  rows=make_rows(data,cols)
  return f"<h1>{title}</h1><table>{header}{rows}</table>"

def top_calc():
  ans=[]
  ans.append(make_table([
    calc_iver('einat/yigal/timber',100),
    calc_iver('theadore',23),
    calc_iver('audrey',50),
    calc_iver('cat',3)
  ],'ivermectin'))

  ans.append(make_table([
    calc_guard('einat/yigal/timber',100),
    calc_guard('theadore',23),
    calc_guard('audrey',50),
    calc_guard('cat',3)
  ],'safe gurard'))  
  return '\n'.join(ans)





      

with open('template.html', 'r', encoding='utf-8') as file:
    template = file.read()
content=template.replace('content',top_calc())
with open('index.html', 'w', encoding='utf-8') as file:
    file.write(content)
