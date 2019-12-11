#!/bin/python3

import math
import os
import random
import re
import sys

#enhanced hash map that can add integers to all keys and retain mapping to
#same values in O(1) time, as well as add decimal numbers to all values and
#retain mapping to the original keys in O(1) time
class additionHashMap():
    def __init__(self, k, v):
        self.k_mod = k
        self.v_mod = v
        self.map = {}

    def set_val(self, key, val):
        #mod_key is the total addition/subtraction value removed from the
        #requested key value - so if k_mod is 2 and key is 5, the mod_key
        #map key that should be stored in self.map is 3
        mod_key = key-self.k_mod
        #the map must assign value given ("val") minus the value modifier
        #("self.v_mod") since the value modifier is added to all values
        #in the map when the value is extracted using the "get" method below
        self.map[mod_key]=val-self.v_mod

    def get_val(self, key):
        #mod_key is the total addition/subtraction value removed from the
        #requested key value - so if k_mod is 2 and key is 5, the mod_key
        #map key that should be stored in self.map is 3
        mod_key = key-self.k_mod
        #must subtract the composite "value" shift of self.v_mod from the
        #looked-up value
        return self.map[mod_key]+self.v_mod

    #increases all keys by the value of key_plus (should be an integer)
    def add_to_keys(self, key_plus):
        self.k_mod += key_plus

    #increases all values by the value of val_plus (does not need to be an integer)
    def add_to_vals(self, val_plus):
        self.v_mod += val_plus

    #gives all current keys for the additionHashMap
    def keys(self):
        return [key+self.k_mod for key in self.map.keys()]

    def values(self):
        return [val+self.v_mod for val in self.map.values()]


if __name__ == '__main__':
    map_check = additionHashMap(0, 0)
    map_check.set_val(1, 1)
    #map => {1:1}
    map_check.add_to_vals(2)
    #map => {1:3}
    map_check.set_val(3, 3)
    #map => {1:3, 3:3}
    print(map_check.get_val(1))
    #=> 3
    map_check.add_to_vals(-5)
    #map => {1:-2, 3:-2}
    print(map_check.get_val(3))
    #=> -2
    map_check.add_to_keys(-3)
    #map => {-2:-2, 0:-2}
    print(map_check.get_val(0))
    #=> -2
    map_check.add_to_vals(-5)
    #map => {-2:-7, 0:-7}
    print(map_check.get_val(0))
    #=> -7
    print(map_check.get_val(-2))
    #=> -7
    map_check.set_val(0, 1)
    #map => {-2:-7, 0:1}
    print(map_check.map, map_check.k_mod)
    print(map_check.get_val(0))
    #=> 1
    map_check.set_val(1, 10)
    #map => {-2:-7, 0:1, 1:10}
    print(map_check.map, map_check.k_mod)
    map_check.get_val(1)
    print(map_check.map)
    map_check.set_val(-5, 3)
    print(map_check.map)
    #map => {-2:-7, 0:1, 1:10, -5:3}
    map_check.add_to_keys(5)
    #map => {3:-7, 5:1, 6:10, 0:3}
    map_check.add_to_vals(7)
    #map => {3:0, 5:8, 6:17, 0:10}
    print(map_check.keys())
    for item in map_check.keys():
        print(map_check.get_val(item))
    print(map_check.values())
    map_check.set_val(2, 25)
    map_check.set_val(4, 25)
    print(map_check.values())
