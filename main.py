# Author: Daniel Dean dpd5518@psu.edu
# Collaborator: Xiang Liu xfl5249@psu.edu
# Collaborator: Yamin Zhang ykg5402@psu.edu
# Collaborator: Anna Gillard amg73017@psu.edu
# Section: 2
# Breakout: 2

def sum_n(n):
  if n <= 1:
    return(n)
  else:
    return(n + sum_n(n - 1))

def print_n(s,n):
  if n >= 1:
    print(s)
    return print_n(s,n-1)

if __name__ == '__main__':
  def run():
    sum_n(input(""))


