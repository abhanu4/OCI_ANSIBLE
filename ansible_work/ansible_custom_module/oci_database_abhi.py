#!/bin/python

from __future__ import absolute_import, division, print_function

print("Importing future library passed") 

ANSIBLE_METADATA= {
 "metadata_version": "1.0",
 "status": "preview",
 "support": "community"
}

print(ANSIBLE_METADATA)

DOCUMENTATION = """
---
module: oci_database_cust
short_description: Fetches details of one or more Databases
description:
    - Fetches details of one or more OCI Databases.
version_added: "2.5"
options:
     compartment_id: Identifier of compartment in which DB exist
          description: Identifier of compartment in which DB exist
          required: false

author:
    - "Abhishek Rajbhanu(@arajbhan)
extends_documentation_fragment: oracle
"""

EXAMPLES = """
#Fetch DB details
- name: Fetching database details from a compartment
  oci_database_cust:
    compartment_id: 'ocid1.compartment.aaaa' 
"""

print(__name__)

RETURN = """
    databases:
        description: Attributes of the Database.
        returned: success
        type: complex
        contains:
            character_set:
                description: The character set for the database.
                returned: always
                type: string
                sample: AL32UTF8
            compartment_id:
                description: The identifier of the compartment containing the DB System where the Database resides.
                returned: always
                type: string
                sample: ocid1.compartment.oc1.xzvf..oifds
            db_backup_config:
                description: Determines whether to configure automatic backup of the Database.
                returned: always
                type: string
                sample: db_backup_config:{
                            auto_backup_enabled:false
                        }
            db_home_id:
                description: The identifier of the DB Home containing the Database.
                returned: always
                type: string
                sample: ocid1.dbhome.oc1.iad.xxxxxEXAMPLExxxxx
            db_name:
                description: The database name.
                returned: always
                type: string
                sample: ansibledb
            db_unique_name:
                description: A system-generated name for the database to ensure uniqueness within an Oracle Data Guard
                             group (a primary database and its standby databases). The unique name cannot be changed.
                returned: always
                type: string
                sample: ansibledb_iad7b
            db_workload:
                description: Database workload type.
                returned: always
                type: string
                sample: OLTP
            id:
                description: Identifier of the Database.
                returned: always
                type: string
                sample: ocid1.database.oc1.iad.xxxxxEXAMPLExxxxx
            time_created:
                description: Date and time when the DB Node was created, in the format defined by RFC3339
                returned: always
                type: datetime
                sample: 2016-08-25T21:10:29.600Z
            software_storage_size_in_gb:
                description: Storage size, in GBs, of the software volume that is allocated to the DB system. This is
                             applicable only for VM-based DBs.
                returned: always
                type: string
                sample: 1024
            ncharacter_set:
                description: The national character set for the database.
                returned: always
                type: string
                sample: AL16UTF16
            pdb_name:
                description: Pluggable database name. It must begin with an alphabetic character and can contain a
                             maximum of eight alphanumeric characters. Special characters are not permitted. Pluggable
                             database should not be same as database name.
                returned: always
                type: string
                sample: ocid1.vnic.oc1.iad.xxxxxEXAMPLExxxxx
            lifecycle_state:
                description: The current state of the Database.
                returned: always
                type: string
                sample: AVAILABLE
            lifecycle_details:
                description: Additional information about the current lifecycle_state of the Database.
                returned: always
                type: string
                sample: AVAILABLE
        sample: [{
                   "character_set":"AL32UTF8",
                   "compartment_id":"ocid1.compartment.aaaa",
                   "freeform_tags":{"deployment":"test"},
                   "defined_tags":{"target_users":{"division":"design"}},
                   "db_backup_config":{
                            "auto_backup_enabled":false
                    },
                   "db_home_id":"ocid1.dbhome.oc1.iad.xxxxxEXAMPLExxxxx",
                   "db_name":"ansibledbone",
                   "db_unique_name":"ansibledbone_iad2cj",
                   "db_workload":"OLTP",
                   "id":"ocid1.database.oc1.iad.xxxxxEXAMPLExxxxx",
                   "lifecycle_details":null,
                   "lifecycle_state":"BACKUP_IN_PROGRESS",
                   "ncharacter_set":"AL16UTF16",
                   "pdb_name":null,
                   "time_created":"2018-02-22T08:42:26.060000+00:00"
                },
                {
                   "character_set":"AL32UTF8",
                   "compartment_id":"ocid1.compartment.aaaa",
                   "freeform_tags":{"deployment":"production"},
                   "defined_tags":{"target_users":{"division":"development"}},
                   "db_backup_config":{
                            "auto_backup_enabled":true
                    },
                   "db_home_id":"ocid1.dbhome.oc1.iad.xxxxxEXAMPLExxxxx",
                   "db_name":"ansibledbtwo",
                   "db_unique_name":"ansibledbtwo_iad2cj",
                   "db_workload":"OLTP",
                   "id":"ocid1.database.oc1.iad.xxxxxEXAMPLExxxxx",
                   "lifecycle_details":null,
                   "lifecycle_state":"AVAILABLE",
                   "ncharacter_set":"AL16UTF16",
                   "pdb_name":null,
                   "time_created":"2018-02-20T08:42:26.060000+00:00"
                }]

"""


try:
  from oci.database.database_client import DatabaseClient
  from oci.exceptions import ServiceError
  from oci.util import to_dict
  HAS_OCI_PY_SDK = True
except ImportError:
  print('Import Failed')
  HAS_OCI_PY_SDK = False

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils, oci_db_utils


#print('HAS_OCI_PY_SDK',HAS_OCI_PY_SDK)

##########################################
## Defining Main Function ################

def main():
  logger= oci_utils.get_logger('Database_logger')
  print('Type of logger ',type(logger))
  print('Value of logger ',logger)
 ############### set_logger(logger)
  module_args= oci_utils.get_common_arg_spec()
  print('Module args value', module_args)
  print('Module args value',type( module_args))
  
  module_args.update(
  dict(
  compartment_id= dict(type='str', required= False)
  )
  )
  print('######################')

  print('updated module_args',module_args)

  module = AnsibleModule(argument_spec=module_args,  supports_check_mode=True) 
  print("#############################")
  
  if HAS_OCI_PY_SDK == False:
     module.fail_json(msg="oci Python SDK is required for this module") 
  
  db_client= oci_utils.create_service_client(module, DatabaseClient)
  state = module.params["state"]
  if state == 'restore':
    result=restore_database(db_client,module)
  elif state == 'update':
    result = update_database(db_client,module)
  
  module.exit_json(**result)


if __name__ ==  '__main__':
  main()
