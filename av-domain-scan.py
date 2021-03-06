#!/usr/bin/env python
#coding:utf-8
from invRegex import invert
import sys, envoy, itertools

##def generate_domain(input_str):
## if '?' in input_str:
## count = input_str.count('?')
## all_str = negex_str()
## all_combinations = itertools.product(all_str, repeat=count)
## initial_domain = (list(input_str) for i in range(len(all_str)**count))
## for item in initial_domain:
## yield ''.join((replace_wildcard(item, all_combinations.next())))
## else:
## yield input_str
##
##def replace_wildcard(str_list, value):
## value = (item for item in value)
## for key, _value in enumerate(str_list):
## if '?' == _value:
## str_list[key] = value.next()
## return str_list

##def generate_domain(input_str):
##    count = input_str.count('?')
##    if count:
##        prefix, suffix = input_str.split('?'*count)
##        all_str = negex_str()
##        all_combinations = itertools.product(all_str, repeat=count)
##        for combination in all_combinations:
##            yield prefix + ''.join(combination) + suffix
##    else:
##        yield input_str

def check_domain_available(domain):
    r = envoy.run('whois %s'%domain)
    if 'No match for' in r.std_out:
        return True
    return False

def main(input_str):
    prefix, suffix = input_str.split('.')
    for domain in invert(prefix):
        domain = domain + '.' + suffix
        if check_domain_available(str(domain)):
            print domain

if __name__ == "__main__":
    input_str = sys.argv[1]
    main(input_str)
