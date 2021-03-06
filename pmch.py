#    Copyright (C) 2017 Greenweaves Software Pty Ltd
#
#    This is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This software is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with GNU Emacs.  If not, see <http://www.gnu.org/licenses/>
#
#    pmch 	Perfect Matchings and RNA Secondary Structures 

from rosalind import RosalindException,factorial,verify_counts_complete_graph
def NumberPerfectMatchings(string):
 
    counts=verify_counts_complete_graph(string)
    return factorial(counts['A'])*factorial(counts['G'])

if __name__=='__main__':
    print (NumberPerfectMatchings('CGCUUGCAGGACAAGGUGCAUAUCUUCACCAUCAGCUAAACGAUAGCCGCUCACGCGGGAUGGUGCGUUCCGUG'))
