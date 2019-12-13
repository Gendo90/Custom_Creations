import heapq
import sys


#Enhanced heap data structure that uses a map to store value indices and
#remove elements in O(log(n)) time - as compared to O(n) removal time for
#regular heaps, including python's builtin heapq package

#Example uses are Dijkstra's upgraded algorithm, Prim's upgraded MST algorithm

#only works for distinct values right now!
#TODO: extend for multiple identical values by using arrays in the self.indices map
class HeapMap():
    def __init__(self):
        self.indices = {}
        self.heap = []

    def push(self, elem):
        self.heap.append(elem)
        i=len(self.heap)
        #use lists instead of single values for the map from values to indices
        if(elem not in self.indices):
            self.indices[elem] = [i-1]
        else:
            self.indices[elem].append(i-1)
        #bubble-up through heap
        while(elem<self.heap[i//2-1] and i>1):
            #update map of values with new indices
            parent_elem = self.heap[i//2-1]
            self.indices[elem][-1] = i//2-1
            #need to replace the correct parent element index in the list
            #for multiple indices with the same value
            self.indices[parent_elem][self.indices[parent_elem].index(i//2-1)] = i-1
            #update element positions in heap array
            self.heap[i-1], self.heap[i//2-1] = self.heap[i//2-1], self.heap[i-1]
            i=i//2

    def popMin(self):
        result = self.heap.pop(0)
        #remove value from indices map if the minimum value is not -infinity
        if(result!=-float('inf')):
            if(len(self.indices[result])==1):
                self.indices.pop(result)
            else:
                self.indices[result].pop(self.indices[result].index(0))

        if(not self.heap):
            return result
        #get the length of the heap
        heap_size = len(self.heap)

        #replace first element with the last element in balanced heap
        last_elem = self.heap.pop()
        self.heap.insert(0, last_elem)
        self.indices[last_elem][self.indices[last_elem].index(heap_size)] = 0
        #bubble down through heap to get new minimum at position 0
        i=1
        while(i<heap_size):
            if(2*i<=heap_size):
                first_child_ind = 2*i-1
            else:
                break
            if(2*i+1<=heap_size):
                second_child_ind = 2*i
            else:
                second_child_ind=None
            #find the minimum child and its index in the heap to bubble down
            if(second_child_ind==None or self.heap[first_child_ind]<self.heap[second_child_ind]):
                min_child_ind = first_child_ind
            else:
                min_child_ind = second_child_ind
            #switch min child with the parent unless parent is larger
            parent = self.heap[i-1]
            child = self.heap[min_child_ind]
            if(child>=parent):
                break
            else:
                #update values to indices map as an array
                self.indices[child][self.indices[child].index(min_child_ind)] = i-1
                self.indices[parent][self.indices[parent].index(i-1)] = min_child_ind
                self.heap[min_child_ind], self.heap[i-1] = self.heap[i-1], self.heap[min_child_ind]
            i=min_child_ind+1
        return result

    #works in log(n) time due to map keeping track of value indices
    def remove(self, elem):
        if(elem not in self.indices):
            return False
        removal_ind = self.indices[elem][-1]
        self.heap[removal_ind] = -float('inf')
        #remove index from map, and if there are no indices left, remove value
        #key from map
        self.indices[elem].pop()
        if(not self.indices[elem]):
            self.indices.pop(elem)
        #bubble up the -inf value and then remove it!
        i=removal_ind+1
        while(i!=1):
            #update map of values with new parent index as it moves down in the heap
            parent_elem = self.heap[i//2-1]
            self.indices[parent_elem][self.indices[parent_elem].index(i//2-1)] = i-1
            #update element positions in heap array
            self.heap[i-1], self.heap[i//2-1] = self.heap[i//2-1], self.heap[i-1]
            i=i//2

        #now have -inf as the minimum values, so pop it using extract-min operation
        self.popMin()
        #return the element removed
        return elem
