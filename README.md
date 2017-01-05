# check_mk
check_mk Plugins

## galera

## supermicro
Extended SNMP-Checks for supermicro servers, based on Check MK original checks.
Added Checks:
* Memory DIMM (ECC error count and Uncorrectable ECC error count)

Changed Checks:
* Change message of sensors, which have only a state, from numeric to string (State 0 -> State OK)

### Installation
I tested this with Linux Debian 8, Ubuntu should work too.
* install Super Doctor 5 from ftp://ftp.supermicro.com/utility/SuperDoctor_5/. Enable Option 'USE_AGENT_SNMP_EXTENSION'.
* install package 'snmpd'
* add option 'pass  .1.3.6.1.4.1.10876  /opt/Supermicro/SuperDoctor5/libs/native/snmpagent' to /etc/snmp/snmpd.conf
* configure community or create a rouser
* edit /etc/default/snmpd to run snmpd as user root, without this there is trouble with snmpagent above, i don't figured it out
* restart service snmpd
* (re)inventorize your host in Check MK (Change Agent Type to 'Dual: Check_MK Agent + SNMP' and create a rule 'SNMP credentials of monitored hosts' with your community or rouser above
