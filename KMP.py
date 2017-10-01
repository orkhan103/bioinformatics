# Copyright (C) 2017 Greenweaves Software Pty Ltd

# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with GNU Emacs.  If not, see <http://www.gnu.org/licenses/>

# KMP Speeding Up Motif Finding http://rosalind.info/problems/kmp/

def kmp(s):
    '''
    A prefix of a length n string s is a substring s[1:j]; a suffix of s is a substring s[k:n]

    The failure array of s
    is an array P of length n for which P[k] is the length of the longest substring s[j:k]
    that is equal to some prefix s[1:k-j+1], where j cannot equal 1 (otherwise, P[k] would always equal k). By convention, P[1]=0

    Given: A DNA string s (of length at most 100 kbp) in FASTA format.

    Return: The failure array of s
'''
    def longest_substring(k):
        for j in range(1,k):
            if s[j:k]==s[0:k-j]:
                return k-j
        return 0
 
    return [longest_substring(k) for k in range(1,len(s)+1)]

if __name__=='__main__':
    import time
    start=time.time()
    print(kmp('CAGCATGGTATCACAGCAGAG'))

    name=''
    strings=[]
    with open('c:/Users/Weka/Downloads/rosalind_kmp.txt') as f:
        for line in f:
            if (len(name))==0:
                name=line.strip()
            else:
                strings.append(line.strip())
    string=''.join(s for s in strings)

    print(kmp(string))
    elapsed=time.time()-start
    minutes, seconds = divmod(elapsed, 60)
    print (minutes,seconds)    
                