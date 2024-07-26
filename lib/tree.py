class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):

    node_to_visit = [self.root]
    while node_to_visit:
      node = node_to_visit.pop()
      if node['id'] == id:
        return node
      node_to_visit.extend(node['children'])
    
    return None