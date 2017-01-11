class HumanResources(Employee, FullTime):
  """Describes human resources employees"""

  def __init__(self, first_name, last_name):
    # Note that we can't use super() any more because there is
    # more than one class being inherited from. Because of that
    # we have to call the constructor of each parent class individually
    Employee.__init__(first_name, last_name)
    FullTime.__init__()