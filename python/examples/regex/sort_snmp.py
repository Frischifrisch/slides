import sys

def process(filename):
   snmps = []
   with open(filename) as fh:
      snmps.extend({
          'orig': row.rstrip(),
      } for row in fh)
   #print(snmps)

   max_number_of_parts = 0
   max_number_of_digits = 0
   for snmp in snmps:
       snmp['split'] = snmp['orig'].split('.')
       max_number_of_parts  = max(max_number_of_parts, len(snmp['split']))
       for part in snmp['split']:
           max_number_of_digits = max(max_number_of_digits, len(part))

   padding = "{:0" + str(max_number_of_digits)  +  "}"
   #print(padding)
   for snmp in snmps:
      padded_split = snmp['split'] + ['0'] * (max_number_of_parts - len(snmp['split']))

      padded = [padding.format( int(part)) for part in padded_split]
      snmp['padded'] = padded
      snmp['joined'] = '.'.join(padded)


   #print(snmps)
   #print(max_number_of_parts)
   #print(max_number_of_digits)

   snmps.sort(key = lambda e: e['joined'])
   sorted_snmps = [snmp['orig'] for snmp in snmps]
   for snmp in sorted_snmps:
      print(snmp)

# get the max number of all the snmp parts
# make each snmp the same length
# pad each part to that length with leading 0s

if len(sys.argv) < 2:
   exit(f"Usage: {sys.argv[0]} FILENAME")
process(sys.argv[1])

