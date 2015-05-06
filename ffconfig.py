#
# configuration for flowfall
#

ofswitches = [
    {
        "dpid" : 1,
        "vnf_up_ports" : [
            {
                "port_num" : 1,
                "mac" : [ "00:01:01:01:02:00", "00:01:01:01:02:01",
                          "00:01:01:01:02:02", "00:01:01:01:02:03",
                          "00:01:01:01:02:04", "00:01:01:01:02:05",
                          "00:01:01:01:02:06", "00:01:01:01:02:07",
                          ]
                },
            ],

        "vnf_down_ports" : [
            {
                "port_num" : 2,
                "mac" : [ "00:01:01:01:02:00", "00:01:01:01:02:01",
                          "00:01:01:01:02:02", "00:01:01:01:02:03",
                          "00:01:01:01:02:04", "00:01:01:01:02:05",
                          "00:01:01:01:02:06", "00:01:01:01:02:07",
                          ]
                },
            ],

        "non_up_ports" : [
            {
                "port_num" : 3,
                "mac" : [ "00:01:01:01:02:00" ]
                },
            ],

        "non_down_ports" : [
            {
                "port_num" : 4,
                "mac" : [ "00:01:01:01:02:00" ]
                },
            ],
        }
    ]


prefixes = [
    { "prefix" : "45.0.100.0/24", "type" : "CLIENT", },
    { "prefix" : "45.0.101.0/24", "type" : "CLIENT", },
    ]
