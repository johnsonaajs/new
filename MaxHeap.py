class Entry:
  def __init__(self, priority, process_id):
    self.priority = priority
    self.process_id = process_id
  def __repr__(self):
    return f"Entry(priority=(self.priority), process_id=(self.process_id)"
  def __gt__(self, other):
    return self.priority > other.priority
  def __eq__ (self, other):
    return self.priority == other.priority 
class MaxHeap:
    def __init__(self):
        self._heap = []
    def put(self, entry):
        self._heap.append(entry)
        self._unheap(len(self._heap)-1)
    def remove_max(self):
        if len(self._hep)== 0: raise IndexError("Empty heap")
        max_pe = self._heap[0]
        last = self._heap.pop()
        if self._heap:
          self._heap[0]=last 
          self._downheap(0)
        return max_pe.process_id
    def change_priority(self, process_id, new_priority):
        for entry in self._heap:
          if entry.process_id == process_id:
              old_priority= entry.priority
              entry.priority = new_priority 
              if new_priority > old_priority:
                  self._upheap(self._heap.index(entry))
              else:
                  self._downheap(self._heap.index(entry))
              return True
        return False
    def _upheap(self, index):
        while index > 0:
            parent_index = (index -1) // 2
            if self._heap[parent_index] > self._heap[index]:
                break
            self._heap[parent_index], self._heap[index] = self._heap[index], self._heap[parent_index]
            index = parent_index 
    def _downheap(self, index):
        while index * 2 + 1 < len(self._heap):
            left_child_index = index *2+1 
            right_child_index = left_child_index + 1 
            max_child_index = left_child_index 
            if right_child_index < len(self._heap) and self._heap[right_child_index] > self._heap[left_child_index]:
                max_child_index = right_child_index 
            if self._heap[max_child_index] < self._heap[index]:
                break 
            self._heap[max_child_index], self._heap[index] = self._heap[index], self._heap[max_child_index]
            index = max_child_index 
    def __len__(self): 
        return len(self._heap)
class TaskManger:
    def __init__(self):
        self.processor_queue = MaxHeap()
    def add_process(self, entry):
        self.processor_queue.put(entry)
    def remove_process(self):
        return self.processor_queue.remove_max()
